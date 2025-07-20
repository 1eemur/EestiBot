"""
Translation service using Google Translator
"""

import logging
from deep_translator import GoogleTranslator


class TranslationService:
    """Service for translating text between languages"""
    
    @staticmethod
    def translate(text: str, source: str = "et", target: str = "en") -> str:
        """
        Translate text from source language to target language
        
        Args:
            text: Text to translate
            source: Source language code (default: Estonian)
            target: Target language code (default: English)
            
        Returns:
            Translated text, or original text if translation fails
        """
        try:
            translator = GoogleTranslator(source=source, target=target)
            return translator.translate(text)
        except Exception as e:
            logging.error(f"Translation error: {e}")
            return text