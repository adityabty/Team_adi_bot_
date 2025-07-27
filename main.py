from pyrogram import Client, filters
from config import BOT_TOKEN, API_ID, API_HASH
from welcome import send_welcome
from player import play_command, skip_command, queue_command, stop_command

app = Client("musicbot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await send_welcome(_, message)

@app.on_message(filters.command("play") & (filters.group | filters.private))
async def cmd_play(_, message):
    await play_command(_, message)

@app.on_message(filters.command("skip") & filters.group)
async def cmd_skip(_, message):
    await skip_command(_, message)

@app.on_message(filters.command("queue") & filters.group)
async def cmd_queue(_, message):
    await queue_command(_, message)

@app.on_message(filters.command("stop") & (filters.group | filters.private))
async def cmd_stop(_, message):
    await stop_command(_, message)

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
