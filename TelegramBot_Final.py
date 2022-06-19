from ast import Call
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import urllib.request
from PIL import Image
import telepot
import subprocess
import requests
urllib.request.urlretrieve(
    'http://192.168.137.132/photo',
    "gfg.png")

img = Image.open("gfg.png")
updater = Updater("5504579287:AAEdNLIDMXMZgj6tUjnS1ReemBgBIvaReP0",
                  use_context=True)

Bot = telepot.Bot('5504579287:AAEdNLIDMXMZgj6tUjnS1ReemBgBIvaReP0')
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
            "Hello sir, Welcome to the Bot.Please write\
		/help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /pasteImage to get Image in chat
	/getImage to get Image URL""")


def image_url(update: Update, context: CallbackContext):
    
    update.message.reply_text(
            "Photo URL => \
		http://192.168.137.132/photo")

def send_photo(update:Update,context:CallbackContext):
    urllib.request.urlretrieve(
    'http://192.168.137.132/photo',
    "gfg.jpg")

    chat_id="-1001624381132"
    Bot.sendPhoto(chat_id, photo=open('gfg.jpg', 'rb'))




def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('getImage', image_url))
updater.dispatcher.add_handler(CommandHandler('pasteImage', send_photo))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))

updater.dispatcher.add_handler(MessageHandler(
    Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
