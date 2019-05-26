def is_word_capitalized(word):
    """
    Check if word is capitalized.

    Args:
        word (str): Word.

    Returns:
        (boole): True f word is capitalized. False otherwise.

    """
    if not word:
        return False

    first_letter = word[0]
    return first_letter == first_letter.upper()


def get_chat_id(update):
    """
    Get chat ID from update.

    Args:
        update (instance): Incoming update.

    Returns:
        (int, None): Chat ID.

    """
    # Simple messages
    if update.message:
        return update.message.chat_id

    # Menu callbacks
    if update.callback_query:
        return update.callback_query.message.chat_id

    return None
