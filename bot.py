from telegram.ext import Updater, CommandHandler


def start(update, context):

    update.message.reply_text('Hola, humano!')

    
