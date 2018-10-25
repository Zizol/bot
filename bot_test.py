from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,
                        InlineQueryHandler
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
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)
    

#Add handlers (/start, message) to the dispatcher. Allows passing arguments for /caps
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)
inline_caps_handler = InlineQueryHandler(inline_caps)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(inline_caps_handler)

#Activate bot
updater.start_polling()
