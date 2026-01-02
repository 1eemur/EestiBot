"""
General commands cog for EestiBot
"""

from discord.ext import commands


class General(commands.Cog):
    """General utility and information commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='hommik')
    async def hommik(self, ctx):
        """Send a friendly Estonian greeting"""
        await ctx.send("hommik!")
    
    @commands.command(name='sourcecode', aliases=['lähtekood'])
    async def source_code(self, ctx):
        """Display link to bot's source code"""
        await ctx.send('*GitHub Repo*: <https://github.com/1eemur/EestiBot>')
    
    @commands.command(name='quickstart', aliases=['qs'])
    async def quickstart(self, ctx):
        """Display Estonian learning resources"""
        message = (
            "***If you want to start learning you could use:***\n"
            "<https://www.keeleklikk.ee>\n"
            "or\n"
            "<https://www.speakly.me>\n"
            "Keeleklikk is free and Speakly is paid with a two-week free trial "
            "and discount codes available.\n"
            "code FNS7 to get 40% off \n"
            "*For a full Estonian resource list, you can take a look at: "
            "<https://eestikeelt.com>*"
        )
        await ctx.send(message)
    
    @commands.command(name='speakly')
    async def speakly(self, ctx):
        """Display Speakly information"""
        await ctx.send('The codes for free access to Speakly are sadly no longer valid. :(')
    
    @commands.command(name='kuskustkuhu')
    async def kus_kust_kuhu(self, ctx):
        """Explain the difference between kus, kust, kuhu"""
        message = (
            "Kus = where\n"
            "Kuhu = where (to)\n"
            "Kust = where (from)\n\n"
            "Kus sa oled? - Where are you?\n"
            "Kuhu sa lähed? - Where you going?\n"
            "Kust sa pärit oled? - Where are you from?"
        )
        await ctx.send(message)
    
    @commands.command(name='listcommands')
    async def list_commands(self, ctx):
        """List key translation commands"""
        message = (
            "**Key Translation Commands (use !help for the full command list):**\n"
            "!hommik - Show a friendly greeting\n"
            "!cases/!c [word] - Show cases for [word]\n"
            "!define/!d [word] - Show Estonian definitions for [word]\n"
            "!edefine/!ed [word] - Show English translated definitions for [word]\n"
        )
        await ctx.send(message)

    @commands.command(name='tallinn-todo', aliases=['tallinn'])
    async def tallinn_todo(self, ctx):
        """Recommendations for things to do in Tallinn"""
        message = (
            "**Cool neighborhoods to explore**\n"
            "- Old Town\n"
            "<https://maps.app.goo.gl/eZdywW2siDcUVQKQ6>\n"
            "- Telliskivi\n"
            "<https://maps.app.goo.gl/Cy1o376mGucndjH67>\n"
            "- Rottermanni Quarter\n"
            "<https://maps.app.goo.gl/sQS5gr6Zpx7r2vB36>\n"
            "- Kalamaja\n"
            "<https://maps.app.goo.gl/XPoGegyUCh3fXr9j8>\n"
            "- Kadriorg\n"
            "<https://maps.app.goo.gl/6cqQXR2mPqZbHYEv7>\n"
            "**Sights**\n"
            "- Freedom Square\n"
            "<https://maps.app.goo.gl/AfVcyjj2gZjszSQd9>\n"
            "- Patkuli viewing platform\n"
            "<https://maps.app.goo.gl/muKxXNYjdX8LGXfR6>\n"
            "- Kohtuotsa viewing platform\n"
            "<https://maps.app.goo.gl/yr4ZbezsJ7rx9yna9>\n"
            "- Alexander Nevsky Cathedral\n"
            "<https://maps.app.goo.gl/AHRapj9F7SFEk8Xc7>\n"
            "- Danish Kings Garden\n"
            "<https://maps.app.goo.gl/9eB2o3qWH7sr33hi9>\n"
            "- Katarina Gild\n"
            "<https://maps.app.goo.gl/5ihVTusXJxCSBXvi9>\n"
            "- Hellemann Tower and Town Wall Walkway\n"
            "<https://maps.app.goo.gl/ETFQtqURxLFYEqi3A>\n"
            "- Viru Gate\n"
            "<https://maps.app.goo.gl/whkjsqNmP7zKRrgb8>\n"
            "- Balti Jaama Market\n"
            "<https://maps.app.goo.gl/236s9NfR7jLhPaMX9>\n"
            "- Linnahall\n"
            "<https://maps.app.goo.gl/UtBDo4zkXaYCxDCy8>\n"
            "**Walks**\n"
            "- Harbor front, from Linnahall to Noblessner\n"
            "<https://maps.app.goo.gl/mbjACpnQRyRU5gft7>\n"
            "<https://maps.app.goo.gl/fLhtgSw4qr6C24m19>\n"
            "- Kadriorg Park\n"
            "<https://maps.app.goo.gl/HYNXTZxpiJEhGqPb9>\n"
            "- Pirita Beach promenade\n"
            "<https://maps.app.goo.gl/LDHCegDVs6AYiNry6>\n"
            "**History and Art Museums**\n" 
            "- Kiek in de Kök Museum & Bastion Tunnels\n"
            "<https://maps.app.goo.gl/5esukQtMU7ebgkLF7>\n"
            "- Estonian Maritime Museum\n"
            "<https://maps.app.goo.gl/TDGidKTRw8DWWM7V7>\n"
            "- Vabamu Museum of Occupations and Freedom\n"
            "<https://maps.app.goo.gl/arGFmz4MKPW44Luw5>\n"
            "- PoCo Pop And Contemporary Art Museum\n"
            "<https://maps.app.goo.gl/utP8piS4yEV5UNm88>\n"
            "- KUMU Art Museum\n"
            "<https://maps.app.goo.gl/fyXSQVpYzCNEN8767>\n"
        )
        await ctx.send(message)

    @commands.command(name='tallinn-food', aliases=['tallinn-süüa'])
    async def tallinn_food(self, ctx):
        """Recommendations for places to eat in Tallinn"""
        message = (
            "**Kohvikud/Cafés**\n"
            "- Pulla Bakery\n"
            "<https://maps.app.goo.gl/PaNUj9RYsD5ndnVNA>\n"
            "- RØST Bakery\n"
            "<https://maps.app.goo.gl/bJKE9zHBNuEtSsYHA>\n"
            "- Cafe Maiaskmokk\n"
            "<https://maps.app.goo.gl/VrBfE42JotRdg26X8>\n"
            "- Pierre Chocolaterie\n"
            "<https://maps.app.goo.gl/bnBWxiMP9RereUKbA>\n"
            "**Restoranid/Restaurants**\n"
            "- Ramen Taro ($$)\n"
            "<https://maps.app.goo.gl/iHsYTstj189mDBrA7>\n"
            "- Restaurant Nok Nok ($$$)\n"
            "<https://maps.app.goo.gl/we6vU8jRSDvn3Pje8>\n"
        )
        await ctx.send(message)

async def setup(bot):
    """Set up the General cog"""
    await bot.add_cog(General(bot))
