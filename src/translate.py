from functools import lru_cache

from .constants import VOWELS
from .decorators import check_if_word_capitalized
from .rules import vowel_rule, h_rule, consonant_rule


@lru_cache(maxsize=50)
@check_if_word_capitalized
def translate(word):
    """
    Translation strategy selection function.

    Args:
        word (str): Word to translate.

    Returns:
        (str): Translated word.

    """
    if not word:
        return ""

    first_symbol = word[0].lower()

    if first_symbol in VOWELS:
        return vowel_rule(word)

    # Special rules for words
    # started with "h"
    if first_symbol == "h":
        return h_rule(word)

    return consonant_rule(word)
