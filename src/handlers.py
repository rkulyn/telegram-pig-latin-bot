import re
import telegram

from emoji import emojize

from .decorators import emulate_typing
from .translate import translate
from .utils import get_chat_id


@emulate_typing
def start_handler(bot, update, **session_data):
    """
    Start command handler.
    Send greeting message.

    Args:
        bot (instance): Bot.
        update (instance): Incoming update.
        session_data (dict): Session data.

    Returns: None.

    """
    message = (
        "<b>Hello there!</b>\n\n"
        "I'm Pig Latin Translation Bot. \n\n"
        "Type /help to get more information. \n\n"
        "Please, enter the word below to get translation. \n"
    )

    bot.send_message(
        text=message,
        chat_id=get_chat_id(update),
        parse_mode=telegram.ParseMode.HTML
    )


@emulate_typing
def word_handler(bot, update, **session_data):
    """
    Input word handler.
    Send translated word or error message.

    Args:
        bot (instance): Bot.
        update (instance): Incoming update.
        session_data (dict): Session data.

    Returns: None.

    """
    text = update.message.text.strip()
    tokens = re.split(r"(\W)", text)
    words = map(lambda t: t if not re.search(r"\w", t) else translate(t), tokens)
    translation = ''.join(words)
    text = emojize(
        f":pig: {translation}"
        if translation
        else ":disappointed: Failed to translate text.",
        use_aliases=True
    )

    bot.send_message(
        chat_id=get_chat_id(update),
        text=text,
    )


@emulate_typing
def help_handler(bot, update, **session_data):
    """
    Help handler.
    Send help message.

    Args:
        bot (instance): Bot.
        update (instance): Incoming update.
        session_data (dict): Session data.

    Returns: None.

    """
    message = emojize(
        "<b>HELP INFORMATION</b>\n\n"
        "<b>TRANSLATION RULES:</b> \n\n"
        ":small_blue_diamond: If word starts with consonant or consonant cluster, "
        "move first consonant symbols to the end and add <b>\"ay\"</b> \n"
        ":small_blue_diamond: If word starts with vowel, just add <b>\"way\"</b> to the end. \n"
        ":small_blue_diamond: If word starts with <b>\"h\"</b> symbol, "
        "there can be special cases to handle this word. "
        "It's applicable when silent symbol in english words is appeared. "
        "For example <b>\"honest\"</b> word has silent <b>\"h\"</b>. \n\n"
        "<b>COMMANDS:</b> \n\n"
        ":small_orange_diamond: Start command: \n"
        "/start \n"
        ":small_orange_diamond: Help command: \n"
        "/help \n\n"
        "<b>CONTACTS:</b> \n\n"
        "Email for support and feedback related to BOT: <b>rk.social.services@gmail.com</b>. \n\n"
        "License: MIT. \n\n",
        use_aliases=True
    )

    bot.send_message(
        text=message,
        chat_id=get_chat_id(update),
        disable_web_page_preview=True,
        parse_mode=telegram.ParseMode.HTML,
    )
