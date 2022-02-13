from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

with open('./token.txt') as f:
    token = f.readline()

updater = Updater(token.strip())

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()