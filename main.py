from configparser import ConfigParser
from utils import setup_logger
from pyrogram import Client, filters
from pyrogram.types import Message

logger = setup_logger("main")

config = ConfigParser()
config.read('default_config.ini')
api_key = config.get('Telegram', 'API_ID')
api_secret = config.get('Telegram', 'API_HASH')
username = config.get('Telegram', 'USERNAME')
user_input_channel = int(config.get('Telegram', 'TARGET_GROUP'))

app = Client(username, api_key, api_secret)

# Define filters for incoming messages
@app.on_message(filters.chat(user_input_channel))
async def new_message_listener(client, message):
    try:
        print(f'Time sent to telegram : {message.date}')
        print(f'Received new message : {message.text}')
        logger.info(f'Time sent to telegram : {message.date}')
        logger.info(f'Received new message : {message.text}')

        
    except Exception as e:
        print(f'Error in new_message_listener : {e}')

# Start the Pyrogram client
app.run()
