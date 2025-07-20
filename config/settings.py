"""
Configuration settings for EestiBot
"""

import os
from configparser import ConfigParser
from pathlib import Path


class Settings:
    """Bot configuration settings"""
    
    def __init__(self):
        self.config = ConfigParser()
        self._load_config()
        
    def _load_config(self):
        """Load configuration from constants.ini file"""
        config_path = Path(__file__).parent / "constants.ini"
        
        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}\n"
                "Please create constants.ini with your bot token."
            )
        
        self.config.read(config_path)
        
    @property
    def bot_token(self) -> str:
        """Get Discord bot token"""
        try:
            return self.config.get("CONSTANTS", "BOTTOKEN")
        except Exception as e:
            raise ValueError(
                "Bot token not found in constants.ini. "
                "Please ensure BOTTOKEN is set in the [CONSTANTS] section."
            ) from e