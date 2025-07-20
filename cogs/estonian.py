"""
Estonian language commands cog for EestiBot
"""

from discord.ext import commands
from typing import Optional

from services.api_service import EstonianAPIService
from services.translation_service import TranslationService
from utils.helpers import EstonianWordProcessor


class Estonian(commands.Cog):
    """Estonian language learning and dictionary commands"""
    
    def __init__(self, bot):
        self.bot = bot
        self.api_service = EstonianAPIService()
        self.translation_service = TranslationService()
        self.word_processor = EstonianWordProcessor()
    
    @commands.command(name='cases', aliases=['c'])
    async def cases(self, ctx, *, word: str):
        """Show grammatical cases for an Estonian word"""
        result = self._search_cases(word)
        await ctx.send(result)
    
    @commands.command(name='define', aliases=['d'])
    async def define(self, ctx, *, word: str):
        """Show Estonian definitions for a word"""
        result = self._define_word('est', word)
        await ctx.send(result)
    
    @commands.command(name='edefine', aliases=['ed'])
    async def english_define(self, ctx, *, word: str):
        """Show English translated definitions for a word"""
        result = self._define_word('eng', word)
        await ctx.send(result)
    
    def _search_cases(self, word: str) -> str:
        """
        Search for grammatical cases of an Estonian word
        
        Args:
            word: The word to search cases for
            
        Returns:
            Formatted string with word cases
        """
        data = self.api_service.search_word(word)
        
        if not self._validate_api_response(data):
            return "No definitions found (Make sure to use the word in its root form)"
        
        cases, _, _ = self.word_processor.extract_word_cases(data)
        return cases
    
    def _define_word(self, mode: str, word: str) -> str:
        """
        Get definitions for an Estonian word
        
        Args:
            mode: Either 'est' for Estonian or 'eng' for English translations
            word: The word to define
            
        Returns:
            Formatted string with word definitions
        """
        data = self.api_service.search_word(word)
        
        if not self._validate_api_response(data):
            return "No definitions found (Make sure to use the word in its root form)"
        
        cases, estonian_pos, english_pos = self.word_processor.extract_word_cases(data)
        
        # Build the result header
        if mode == "est":
            result = f"{data['estonianWord'].capitalize()} - {estonian_pos}\n{cases}\n"
        else:
            result = f"{data['estonianWord'].capitalize()} - {english_pos}\n{cases}\n"
        
        # Add definitions
        meanings = data['searchResult'][0].get('meanings', [])
        for i, meaning in enumerate(meanings):
            result += f"🇪🇪 **{i + 1}.** {meaning['definition']}\n"
            
            if mode == 'eng':
                english_def = self.translation_service.translate(meaning['definition'])
                result += f"🇬🇧 **{i + 1}.** {english_def}\n"
        
        return result
    
    @staticmethod
    def _validate_api_response(data) -> bool:
        """
        Validate that API response contains expected data structure
        
        Args:
            data: API response data to validate
            
        Returns:
            True if valid, False otherwise
        """
        return (
            data is not None and 
            isinstance(data, dict) and 
            "searchResult" in data and
            len(data["searchResult"]) > 0
        )


async def setup(bot):
    """Set up the Estonian cog"""
    await bot.add_cog(Estonian(bot))