import config
from telegram.ext import (
    Updater, 
    CommandHandler,
)
from handlers.start import start


def main() -> None:
    updater = Updater(config.TOKEN)

    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler('start', start))

    # Message Handlers

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
