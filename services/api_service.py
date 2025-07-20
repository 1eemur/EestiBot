"""
API service for Estonian dictionary lookups
"""

import requests
import logging
from typing import Optional, Dict, Any

from utils.helpers import sanitize_input


class EstonianAPIService:
    """Service for interacting with the Estonian dictionary API"""
    
    BASE_URL = "https://api.sonapi.ee/v2"
    
    @classmethod
    def search_word(cls, word: str) -> Optional[Dict[str, Any]]:
        """
        Search for a word in the Estonian dictionary API
        
        Args:
            word: The word to search for
            
        Returns:
            Dictionary data if found, None otherwise
        """
        sanitized_word = sanitize_input(word)
        url = f"{cls.BASE_URL}/{sanitized_word}"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 404:
                logging.info(f"Invalid input for word: {word}")
                return None
            elif response.status_code == 400:
                logging.info(f"Word not found: {word}")
                return None
            elif response.status_code == 200:
                return response.json()
            else:
                logging.warning(f"Unexpected status code {response.status_code} for word: {word}")
                return None
                
        except requests.RequestException as e:
            logging.error(f"API request failed for word '{word}': {e}")
            return None
        except ValueError as e:
            logging.error(f"Failed to parse JSON response for word '{word}': {e}")
            return None