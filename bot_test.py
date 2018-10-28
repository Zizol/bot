#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging

#Log issues
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Authentication token obtained through botfather
Token = "749231366:AAFs4JxqBW-OBZGcf8BaqjwMtQIHdsHRQkM"

#Initialize and link updater (input) and dispatcher (output)
updater = Updater(token=Token)
dispatcher = updater.dispatcher

#Function to activate on sending /start, a message, /caps... to the bot
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.from_user.first_name)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

from telegram.error import (TelegramError, Unauthorized, BadRequest,
                            TimedOut, ChatMigrated, NetworkError)

# def error_callback(bot, update, error):
#     try:
#         raise error
#     except Unauthorized:
#         print("allo")
#         # remove update.message.chat_id from conversation list
#     except BadRequest:
#         print("allo")
#         # handle malformed requests - read more below!
#     except TimedOut:
#         print("allo")
#         # handle slow connection problems
#     except NetworkError:
#         print("allo")
#         # handle other connection problems
#     except ChatMigrated as e:
#         print("allo")
#         # the chat_id of a group has changed, use e.new_chat_id instead
#     except TelegramError:
#         print("allo")
#         # handle all other telegram related errors
#
# dispatcher.add_error_handler(error_callback)



#Add handlers (/start, message) to the dispatcher. Allows passing arguments for /caps
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handler)

#Activate bot
updater.start_polling()
