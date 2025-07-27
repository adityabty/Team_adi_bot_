import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP")
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL")
OWNER_HANDLE = os.getenv("OWNER_HANDLE")
ADD_BOT_LINK = os.getenv("ADD_BOT_LINK")
