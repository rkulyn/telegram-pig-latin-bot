import telegram

from functools import wraps

from .utils import (
    is_word_capitalized,
    get_chat_id
)


def check_if_word_capitalized(translate_func):
    """
    Check if word is capitalized
    before translation
    and fix translated word to be consistent.

    Args:
        translate_func (callable): Decorated func (translate).

    """
    @wraps(translate_func)
    def decorated(word):
        result = translate_func(word)
        return result.capitalize() if is_word_capitalized(word) else result

    return decorated


def emulate_typing(handler):
    """
    Send "typing..." message
    when handler is being processed.

    Args:
        handler (callable): Decorated handler.

    """
    @wraps(handler)
    def decorated(bot, update, **session_data):
        bot.send_chat_action(
            chat_id=get_chat_id(update),
            action=telegram.ChatAction.TYPING
        )
        return handler(bot, update, **session_data)

    return decorated


def log_non_admin_users(logger, admin_id):
    """
    Log all incoming non-admin users.
    (For statistic only).

    Args:
        logger (instance): Logger.
        admin_id (int): Admin ID.

    Returns:
        handler (callable): Decorated handler.

    """
    def decorator(handler):

        @wraps(handler)
        def decorated(bot, update, **session_data):
            user_id = update.effective_user["id"]
            if user_id != admin_id:
                logger.info(f"User connected ({update.effective_user}).")
            return handler(bot, update, **session_data)

        return decorated

    return decorator
