"""
EestiBot - Estonian Learning Discord Bot
Main entry point for the bot
"""

import asyncio
import logging
from pathlib import Path

import discord
from discord.ext import commands

from config.settings import Settings


def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


async def load_cogs(bot: commands.Bot):
    """Load all cog modules"""
    cogs = ['cogs.general', 'cogs.estonian', 'cogs.fun']
    
    for cog in cogs:
        try:
            await bot.load_extension(cog)
            logging.info(f"Loaded cog: {cog}")
        except Exception as e:
            logging.error(f"Failed to load cog {cog}: {e}")


async def main():
    """Main bot initialization and startup"""
    setup_logging()
    
    # Initialize settings
    settings = Settings()
    
    # Set up bot intents
    intents = discord.Intents.default()
    intents.message_content = True
    
    # Initialize bot
    bot = commands.Bot(command_prefix='!', intents=intents)
    
    @bot.event
    async def on_ready():
        logging.info(f'Bot logged in as {bot.user} (ID: {bot.user.id})')
        logging.info('------')
    
    # Load cogs
    await load_cogs(bot)
    
    # Start the bot
    try:
        await bot.start(settings.bot_token)
    except KeyboardInterrupt:
        logging.info("Bot shutdown requested")
    except Exception as e:
        logging.error(f"Bot error: {e}")
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())