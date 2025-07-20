"""
Fun commands cog for EestiBot
"""

from discord.ext import commands


class Fun(commands.Cog):
    """Fun and entertainment commands"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='clearskies')
    async def clear_skies(self, ctx):
        """Display ClearSkies image"""
        await ctx.send('https://imgur.com/IckaDkr')
    
    @commands.command(name='theia')
    async def theia(self, ctx):
        """Display Theia GIF"""
        await ctx.send('https://i.imgur.com/i8cUawK.gif')
    
    @commands.command(name='alatiolnud')
    async def alati_olnud(self, ctx):
        """Display 'alati olnud' video"""
        await ctx.send('https://i.imgur.com/8USHKLS.mp4')
    
    @commands.command(name='alatihommik')
    async def alati_hommik(self, ctx):
        """Display 'siin on alati hommik' image"""
        await ctx.send('https://i.imgur.com/1bpeuE4.png')


async def setup(bot):
    """Set up the Fun cog"""
    await bot.add_cog(Fun(bot))