import logging

from telegram.ext import (
    Updater, CommandHandler,
    MessageHandler,
    Filters
)

from src.config import get_config
from src.decorators import log_non_admin_users
from src.handlers import (
    start_handler,
    word_handler,
    help_handler,
)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    config = get_config()

    # Enable logging
    logging.basicConfig(
        format=config.LOGGER_FORMAT,
        level=config.LOGGER_LEVEL
    )

    logger = logging.getLogger("Pig Latin Bot")

    updater = Updater(config.BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Attach handlers to dispatcher
    dp.add_handler(CommandHandler(
        command="start",
        callback=log_non_admin_users(
            logger,
            config.ADMIN_ID
        )(start_handler),
    ))

    dp.add_handler(CommandHandler(
        command="help",
        callback=help_handler
    ))

    dp.add_handler(MessageHandler(
        filters=Filters.text,
        callback=word_handler,
        pass_user_data=True
    ))

    # Log all errors
    dp.add_error_handler(
        lambda bot, update, error:
        logger.error(f'An error occurred. BOT: "{bot}". DETAILS: "{error}".')
    )

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
