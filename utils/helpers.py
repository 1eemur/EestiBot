"""
Utility functions and helpers
"""

import re
from typing import Dict, Any, Tuple


def sanitize_input(text: str) -> str:
    """
    Sanitize input by removing non-alphabetic characters
    
    Args:
        text: Input text to sanitize
        
    Returns:
        Sanitized text containing only Estonian alphabet characters
    """
    return re.sub(r"[^a-zA-ZäÄöÖüÜõÕšŠžŽ]", "", text)


class EstonianWordProcessor:
    """Utility class for processing Estonian word data"""
    
    # Mapping of Estonian parts of speech to English
    PART_OF_SPEECH_MAP = {
        "Nimisõna": "Noun",
        "Omadussõna": "Adjective", 
        "Tegusõna": "Verb",
        "Määrsõna": "Adverb",
        "Omadussõna nimisõna": "Adjective & Noun",
        "Sidesõna": "Conjunction",
        "Asesõna": "Pronoun",
        "Arvsõna": "Numeral",
        "Hüüdsõna": "Interjection"
    }
    
    # Word forms needed for different parts of speech
    NOUN_FORMS = [
        'ainsuse nimetav', 'ainsuse omastav', 'ainsuse osastav',
        'mitmuse nimetav', 'mitmuse omastav', 'mitmuse osastav'
    ]
    
    VERB_FORMS = [
        'ma-infinitiiv e ma-tegevusnimi', 'da-infinitiiv e da-tegevusnimi',
        'kindla kõneviisi oleviku ainsuse 3.p.', 'kindla kõneviisi lihtmineviku ainsuse 3.p.',
        'mitmeosalise verbi pööratud ja eitatud nud-kesksõna',
        'mineviku umbisikuline kesksõna e tud-kesksõna'
    ]
    
    @classmethod
    def extract_word_cases(cls, data: Dict[str, Any]) -> Tuple[str, str, str]:
        """
        Extract word cases and part of speech from API data
        
        Args:
            data: API response data
            
        Returns:
            Tuple of (cases_string, estonian_pos, english_pos)
        """
        word = data['estonianWord']
        part_of_speech = data['searchResult'][0]['meanings'][0]['partOfSpeech'][0]['value'].capitalize()
        part_of_speech = part_of_speech.split(' ', 1)[0].replace(',', '')
        
        english_pos = cls.PART_OF_SPEECH_MAP.get(part_of_speech, "")
        
        if part_of_speech in ("Nimisõna", "Omadussõna", "Omadussõna nimisõna", "Asesõna"):
            cases = cls._get_noun_cases(data)
        elif part_of_speech == "Tegusõna":
            cases = cls._get_verb_cases(data)
        elif part_of_speech in ("Määrsõna", "Arvsõna", "Sidesõna", "Hüüdsõna"):
            cases = f"*{word}*"
        else:
            cases = "Error with input or API"
            
        return cases, part_of_speech, english_pos
    
    @classmethod
    def _get_word_forms_dict(cls, data: Dict[str, Any], forms_list: list) -> Dict[str, str]:
        """Extract word forms from API data"""
        return {
            form['morphValue']: form['value']
            for form in data['searchResult'][0]['wordForms']
            if form['morphValue'] in forms_list
        }
    
    @classmethod
    def _get_noun_cases(cls, data: Dict[str, Any]) -> str:
        """Get noun case forms"""
        word_forms = cls._get_word_forms_dict(data, cls.NOUN_FORMS)
        
        case_string = (
            f"{word_forms['ainsuse nimetav']}, "
            f"{word_forms['ainsuse omastav']}, "
            f"{word_forms['ainsuse osastav']}; "
            f"{word_forms['mitmuse nimetav']}, "
            f"{word_forms['mitmuse omastav']}, "
            f"{word_forms['mitmuse osastav'].replace(',', '/')}"
        )
        
        return f"*{case_string}*"
    
    @classmethod
    def _get_verb_cases(cls, data: Dict[str, Any]) -> str:
        """Get verb case forms"""
        verb_forms = cls._get_word_forms_dict(data, cls.VERB_FORMS)
        
        verb_string = (
            f"{verb_forms['ma-infinitiiv e ma-tegevusnimi']}, "
            f"{verb_forms['da-infinitiiv e da-tegevusnimi']}; "
            f"{verb_forms['kindla kõneviisi oleviku ainsuse 3.p.']}, "
            f"{verb_forms['kindla kõneviisi lihtmineviku ainsuse 3.p.']}; "
            f"{verb_forms['mitmeosalise verbi pööratud ja eitatud nud-kesksõna']}, "
            f"{verb_forms['mineviku umbisikuline kesksõna e tud-kesksõna']}"
        )
        
        return f"*{verb_string}*"