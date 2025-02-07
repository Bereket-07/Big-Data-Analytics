import pandas as pd
import os
from dotenv import load_dotenv
from telethon.sync import TelegramClient

load_dotenv()
phone = os.environ.get("PHONE")
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")



def load_csv(filename):
    return  pd.read_csv(filename)
def display_basic_info(df):
    print(f"The dataframe has {df.shape[0]} rows and {df.shape[1]} columns.")
    print(df.info())
    print(df.describe())
async def scrape_message(channel_username , client):
    await client.start()
    channel = await client.get_entity(channel_username)
    messages = []
    async for message in client.iter_messages(channel , limit=1000):
        messages.append([message.date , message.sender_id , message.text])
    df_telegram = pd.DataFrame(messages , columns=['date', 'sender_id', 'text'])
    df_telegram.to_csv("../data/telegram_data.csv" , index = False)

def extract_tg_data(channel_username):
    client = TelegramClient(phone, api_id, api_hash)
    with client:
        client.loop.run_until_complete(scrape_message(channel_username , client))
