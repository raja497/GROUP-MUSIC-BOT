from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Jason](https://t.me/abhinasroy).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 𝗢𝗪𝗡𝗘𝗥 🛠", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "💬 𝗚𝗥𝗢𝗨𝗣", url="https://t.me/DOSTI_GROUP_1234"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/ABOUT_ABHINAS"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝗔𝗗𝗗 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 ➕", url="https://t.me/http://t.me/Music_abhinasroy_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="https://t.me/ABOUT_ABHINAS")
                ]
            ]
        )
   )


