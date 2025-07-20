import discord
from discord.ext import commands
import os
import requests
import json
import re
from deep_translator import GoogleTranslator
from configparser import ConfigParser

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
constants = ConfigParser()
constants.read("constants.ini")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


def get_translation(text, source="et", target="en"):
    try:
        return GoogleTranslator(source=source, target=target).translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def sanitize_input(inp):
    return re.sub(r"[^a-zA-ZäÄöÖüÜõÕšŠžŽ]", "", inp)


def APISearch(inp):
  sanitized_input = sanitize_input(inp)
  varb = f'https://api.sonapi.ee/v2/{sanitized_input}'

  response = requests.get(varb)
  if response.status_code == 404:
    print("Vigane sisend")
    return None
  if response.status_code == 400:
    print("Sõna ei leitud")
    return None
  if response.status_code == 200:
    data = response.json()
    return data


def getCases(data):
  w = data['estonianWord']
  p = data['searchResult'][0]['meanings'][0]['partOfSpeech'][0]['value'].capitalize()
  p = p.split(' ', 1)[0].replace(',', '')
  p_eng_map = {
      "Nimisõna": "Noun",
      "Omadussõna": "Adjective",
      "Tegusõna": "Verb",
      "Määrsõna": "Adverb",
      "Omadussõna nimisõna": "/Adjective & Noun",
      "Sidesõna": "Conjunction",
      "Asesõna": "Pronoun",
      "Arvsõna": "Numeral",
      "Hüüdsõna": "Interjection"
  }
  p_eng = p_eng_map.get(p, "")
  cases = ""
  if p in ("Nimisõna", "Omadussõna", "Omadussõna nimisõna"):
      word_forms_dict = {
          form['morphValue']: form['value']
          for form in data['searchResult'][0]['wordForms']
          if form['morphValue'] in [
              'ainsuse nimetav', 'ainsuse omastav', 'ainsuse osastav',
              'mitmuse nimetav', 'mitmuse omastav', 'mitmuse osastav'
          ]
      }
      verb_str = (
        word_forms_dict['ainsuse nimetav'] + ', ' + 
        word_forms_dict['ainsuse omastav'] + ', ' + 
        word_forms_dict['ainsuse osastav'] + '; ' + 
        word_forms_dict['mitmuse nimetav'] + ', ' + 
        word_forms_dict['mitmuse omastav'] + ', ' + 
        word_forms_dict['mitmuse osastav'].replace(',', '/')
      )
      cases = f"*{verb_str}*"
  elif p == "Tegusõna":
      verb_forms_dict = {
          form['morphValue']: form['value']
          for form in data['searchResult'][0]['wordForms']
          if form['morphValue'] in [
              'ma-infinitiiv e ma-tegevusnimi', 'da-infinitiiv e da-tegevusnimi', 
              'kindla kõneviisi oleviku ainsuse 3.p.', 'kindla kõneviisi lihtmineviku ainsuse 3.p.',
              'mitmeosalise verbi pööratud ja eitatud nud-kesksõna', 
              'mineviku umbisikuline kesksõna e tud-kesksõna'
          ]
      }
      verb_str = (
        verb_forms_dict['ma-infinitiiv e ma-tegevusnimi'] + ', ' +
        verb_forms_dict['da-infinitiiv e da-tegevusnimi'] + '; ' +
        verb_forms_dict['kindla kõneviisi oleviku ainsuse 3.p.'] + ', ' +
        verb_forms_dict['kindla kõneviisi lihtmineviku ainsuse 3.p.'] + '; ' +
        verb_forms_dict['mitmeosalise verbi pööratud ja eitatud nud-kesksõna'] + ', ' +
        verb_forms_dict['mineviku umbisikuline kesksõna e tud-kesksõna']
      )
      cases = f"*{verb_str}*"
  elif p == "Määrsõna":
      cases = f"*{w}*"
  elif p == "Arvsõna":
    cases = f"*{w}*"
  elif p == "Sidesõna":
    cases = f"*{w}*"
  elif p == "Hüüdsõna":
    cases = f"*{w}*"
  elif p == "Asesõna":
    word_forms_dict = {
          form['morphValue']: form['value']
          for form in data['searchResult'][0]['wordForms']
          if form['morphValue'] in [
              'ainsuse nimetav', 'ainsuse omastav', 'ainsuse osastav',
              'mitmuse nimetav', 'mitmuse omastav', 'mitmuse osastav'
          ]
      }
    verb_str = (
      word_forms_dict['ainsuse nimetav'] + ', ' + 
      word_forms_dict['ainsuse omastav'] + ', ' + 
      word_forms_dict['ainsuse osastav'] + '; ' + 
      word_forms_dict['mitmuse nimetav'] + ', ' + 
      word_forms_dict['mitmuse omastav'] + ', ' + 
      word_forms_dict['mitmuse osastav'].replace(',', '/')
    )
    cases = f"*{verb_str}*"
  else:
    cases = "Error with input or API"
  return cases, p, p_eng


def defineWord(mode, input):
  data = APISearch(input)
  if data is None or not isinstance(data, dict) or "searchResult" not in data:
    return "No definitions found (Make sure to use the word in its root form)"
  cases, p, p_eng = getCases(data)
  result = ""
  if mode == "est":
    result = f"{data['estonianWord'].capitalize()} - {p}\n{cases}\n"
  else:
    result = f"{data['estonianWord'].capitalize()} - {p_eng}\n{cases}\n"
  meanings = data['searchResult'][0].get('meanings', [])
  for i, meaning in enumerate(meanings):
      result += f"🇪🇪 **{i + 1}.** {meaning['definition']}\n"
      if mode == 'eng':
        eng_def = get_translation(meaning['definition'])
        result += f"🇬🇧 **{i + 1}.** {eng_def}\n"
  return result


def searchCases(input):
  data = APISearch(input)
  if data is None or not isinstance(data, dict) or "searchResult" not in data:    
      return "No definitions found (Make sure to use the word in its root form)"
  cases, p, p_eng = getCases(data)
  return cases


def run():
  intents = discord.Intents.default()
  intents.message_content = True
  bot = commands.Bot(command_prefix='!', intents=intents)

  @bot.command()
  async def hommik(ctx: commands.Context):
    await ctx.send("hommik!")

  @bot.command()
  async def speakly(ctx: commands.Context):
    await ctx.send(
        'The codes for free access to Speakly are sadly no longer valid. :('
    )

  @bot.command()
  async def sourcecode(ctx: commands.Context):
    await ctx.send(
        '*GitHub Repo*: <https://github.com/1eemur/EestiBot>'
    )

  @bot.command()
  async def lähtekood(ctx: commands.Context):
    await ctx.send(
        '*GitHub Repo*: <https://github.com/1eemur/EestiBot>'
    )

  @bot.command()
  async def quickstart(ctx: commands.Context):
    await ctx.send(
        '***If you want to start learning you could use:***\n<https://www.keeleklikk.ee/index_en.html>\nor\n<https://www.speakly.me/>\nKeeleklikk is free and Speakly is paid with a two-week free trial and discount codes available.\n code FNS7 to get 40% off \n*For a full Estonian resource list, you can take a look at: <http://eestikeelt.com/>*'
    )

  @bot.command()
  async def qs(ctx: commands.Context):
    await ctx.send(
        '***If you want to start learning you could use:***\n<https://www.keeleklikk.ee/index_en.html>\nor\n<https://www.speakly.me/>\nKeeleklikk is free and Speakly is paid with a two-week free trial and discount codes available.\n code FNS7 to get 40% off \n*For a full Estonian resource list, you can take a look at: <http://eestikeelt.com/>*'
    )

  @bot.command()
  async def kuskustkuhu(ctx: commands.Context):
    await ctx.send(
        'Kus = where\nKuhu = where (to)\nKust = where (from)\n\nKus sa oled? - Where are you?\nKuhu sa lähed? - Where you going?\nKust sa pärit oled? - Where are you from?'
    )

  @bot.command()
  async def listcommands(ctx: commands.Context):
    await ctx.send(
        '**Commands:**\n!hommik - Show a friendly greeting\n!cases/!c [word] - Show cases for [word]\n!define/!d [word] - Show Estonian definitions for [word]\n!edefine/!ed [word] - Show English translated definitions for [word]\n'
    )

  @bot.command()
  async def cases(ctx: commands.Context, word: str):
    await ctx.send(searchCases(word))

  @bot.command()
  async def clearskies(ctx: commands.Context):
    await ctx.send('https://imgur.com/IckaDkr')

  @bot.command()
  async def theia(ctx: commands.Context):
    await ctx.send('https://i.imgur.com/i8cUawK.gif')

  @bot.command()
  async def alatiolnud(ctx: commands.Context):
    await ctx.send('https://i.imgur.com/8USHKLS.mp4')

  @bot.command()
  async def alatihommik(ctx: commands.Context):
    await ctx.send('https://i.imgur.com/1bpeuE4.png')

  @bot.command()
  async def c(ctx: commands.Context, word: str):
    await ctx.send(searchCases(word))

  @bot.command()
  async def define(ctx: commands.Context, word: str):
    await ctx.send(defineWord('est', word))

  @bot.command()
  async def d(ctx: commands.Context, word: str):
    await ctx.send(defineWord('est', word))

  @bot.command()
  async def edefine(ctx: commands.Context, word: str):
    await ctx.send(defineWord('eng', word))
  
  @bot.command()
  async def ed(ctx: commands.Context, word: str):
    await ctx.send(defineWord('eng', word))
  
  bot.run(constants.get("CONSTANTS", "BOTTOKEN"))


if __name__ == "__main__":
  run()
