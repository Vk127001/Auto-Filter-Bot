import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, APPROVED 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        markup = InlineKeyboardMarkup(buttons)
        caption = f"<b>{message.from_user.mention()},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {message.chat.title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>"
        await client.send_photo(
            message.from_user.id, 
            photo='https://telegra.ph/file/a706afc296de6da2a40c8.jpg', 
            caption=caption, 
            reply_markup=markup
        )
