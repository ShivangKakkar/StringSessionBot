from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# About Message
@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def about(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )
