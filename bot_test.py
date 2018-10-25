from telegram.ext import Updater, CommandHandler
import logging

#Log issues
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#Authentication token obtained through botfather
Token = "749231366:AAFs4JxqBW-OBZGcf8BaqjwMtQIHdsHRQkM"

#Initialize and link updater (input) and dispatcher (output)
updater = Updater(token=Token)
dispatcher = updater.dispatcher

#Function to activate on sending a message to the bot
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


#Add handler (command /start) to the dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#Activate bot
updater.start_polling()
