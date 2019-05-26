import telegram

from functools import wraps

from .utils import (
    is_word_capitalized,
    get_chat_id
)


def check_if_word_capitalized(func):
    """
    Check if word is capitalized
    before translation
    and fix translated word to be consistent.

    Args:
        func (callable): Decorated func (translate).

    """
    @wraps(func)
    def decorated(word):
        result = func(word)
        return result.capitalize() if is_word_capitalized(word) else result

    return decorated


def emulate_typing(func):
    """
    Send "typing..." message
    when handler is being processed.

    Args:
        func (callable): Decorated handler.

    """
    @wraps(func)
    def decorated(bot, update, **session_data):
        bot.send_chat_action(
            chat_id=get_chat_id(update),
            action=telegram.ChatAction.TYPING
        )
        return func(bot, update, **session_data)

    return decorated
