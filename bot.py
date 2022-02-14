from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import Filters
from telegram.ext import MessageHandler


# Обработчик голосовых сообщений
def handle_voice(update: Update, context: CallbackContext) -> None:
    file = context.bot.getFile(update.message.voice.file_id)
    file.download('./voice.ogg')
    update.message.reply_text(f'Обрабатываем ваше аудио...')


# Токен бота должен находится в файле "token.txt"
with open('./token.txt') as f:
    token = f.readline()

updater = Updater(token.strip())

# Регистрация обработчика голосовых сообщений
updater.dispatcher.add_handler(MessageHandler(Filters.voice, handle_voice))

updater.start_polling()
updater.idle()