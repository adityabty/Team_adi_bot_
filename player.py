from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from pyrogram import Client
from youtubesearchpython import VideosSearch
from yt_dlp import YoutubeDL
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("musicbot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
pytgcalls = PyTgCalls(app)

queue = {}

ydl_opts = {
    'format': 'bestaudio',
    'noplaylist': True,
    'quiet': True,
}

async def play_command(client, message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("Please tell me which song to play.")
    results = VideosSearch(query, limit=1).result()
    if not results['result']:
        return await message.reply_text("No results found.")
    url = results['result'][0]['link']
    info = YoutubeDL(ydl_opts).extract_info(url, download=False)
    audio_url = info['url']
    chat_id = message.chat.id
    if chat_id not in queue:
        queue[chat_id] = []
    queue[chat_id].append((query, audio_url))
    if len(queue[chat_id]) == 1:
        # start playback
        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(audio_url),
            stream_type="local_stream"
        )
        await message.reply_text(f"🎧 Now playing: **{query}**", parse_mode="markdown")
    else:
        await message.reply_text(f"Queued: **{query}**", parse_mode="markdown")

async def skip_command(client, message):
    chat_id = message.chat.id
    if queue.get(chat_id) and len(queue[chat_id]) > 1:
        queue[chat_id].pop(0)
        next_query, next_url = queue[chat_id][0]
        await pytgcalls.change_stream(chat_id, AudioPiped(next_url))
        await message.reply_text(f"⏭️ Skipped. Now playing: **{next_query}**", parse_mode="markdown")
    else:
        await message.reply_text("Nothing more in queue to skip.")

async def queue_command(client, message):
    chat_id = message.chat.id
    q = queue.get(chat_id)
    if not q:
        return await message.reply_text("Queue is empty.")
    text = "🎶 Current queue:\n" + "\n".join([f"{i+1}. {item[0]}" for i, item in enumerate(q)])
    await message.reply_text(text)

async def stop_command(client, message):
    chat_id = message.chat.id
    if queue.get(chat_id):
        queue.pop(chat_id)
        await pytgcalls.leave_group_call(chat_id)
        await message.reply_text("Stopped playback and cleared queue.")
    else:
        await message.reply_text("No active playback.")
