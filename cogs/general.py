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
            "<https://www.speakly.me/>\n"
            "Keeleklikk is free and Speakly is paid with a two-week free trial "
            "and discount codes available.\n"
            "code FNS7 to get 40% off \n"
            "*For a full Estonian resource list, you can take a look at: "
            "<http://eestikeelt.com/>*"
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
        """List all available bot commands"""
        message = (
            "**Commands:**\n"
            "!hommik - Show a friendly greeting\n"
            "!cases/!c [word] - Show cases for [word]\n"
            "!define/!d [word] - Show Estonian definitions for [word]\n"
            "!edefine/!ed [word] - Show English translated definitions for [word]\n"
        )
        await ctx.send(message)


async def setup(bot):
    """Set up the General cog"""
    await bot.add_cog(General(bot))