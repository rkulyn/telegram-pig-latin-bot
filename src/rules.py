from .constants import VOWELS, H_VOWEL_EXCEPTIONS


def h_rule(word):
    """
    If word starts with "h" symbol, there can be special cases to handle this word.
    It's applicable when silent symbol in english words is appeared.
    For example "honest" word has silent "h"
    sound and should be processed as vowel rule.

    Args:
        word (str): Word to translate.

    Returns:
        (str): Translated word.

    """
    if word.lower() in H_VOWEL_EXCEPTIONS:
        return vowel_rule(word)
    return consonant_rule(word)


def consonant_rule(word):
    """
    If word starts with consonant or consonant cluster,
    move first consonant symbols to the end and add "ay".

    Args:
        word (str): Word to translate.

    Returns:
        (str): Translated word.

    """
    suffix = "ay"

    word = word.lower()
    for idx, symbol in enumerate(word):
        if symbol.lower() in VOWELS:
            # When the first vowel symbol is found,
            # return translation
            return word[idx:] + word[:idx] + suffix

    # If there is only one consonant,
    # just return it + "ay"
    return word + suffix


def vowel_rule(word):
    """
    If word starts with vowel, just add "way" to the end.

    Args:
        word (str): Word to translate.

    Returns:
        (str): Translated word.

    """
    return word + "way"
