from pyrogram import types
from config import SUPPORT_GROUP, SUPPORT_CHANNEL, OWNER_HANDLE, ADD_BOT_LINK

async def send_welcome(client, message):
    text = (
        "🎶 _Welcome to Bollywood Music Bot!_\n\n"
        "Enjoy **24/7 Bollywood tunes** in voice chat with your friends 💖"
    )
    keyboard = types.InlineKeyboardMarkup(
        [
            [types.InlineKeyboardButton("Support Group", url=SUPPORT_GROUP)],
            [types.InlineKeyboardButton("Support Channel", url=SUPPORT_CHANNEL)],
            [types.InlineKeyboardButton("Owner", url=f"https://t.me/{OWNER_HANDLE.lstrip('@')}")],
            [types.InlineKeyboardButton("➕ Add Me to Your Group", url=ADD_BOT_LINK)]
        ]
    )
    await message.reply_text(text, reply_markup=keyboard, parse_mode="markdown")
