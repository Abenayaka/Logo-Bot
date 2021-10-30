from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from resources.texts import *
from config import *

bot = Client("Lorum-Bot", 
    bot_token=BOT_TOKEN, 
    api_id=API_ID, 
    api_hash=API_HASH,
    plugins=dict(root="plugins"))

@bot.on_message(filters.command("start"))
async def help(_, update):
    await update.reply_video(
                    video="https://telegra.ph/file/a6f605f70bc9ca7e3dbee.mp4",
                    reply_markup = startbutton,
                    caption = starttext.format(update.from_user.mention))
                     

@bot.on_message(filters.command("help"))
async def help(_, message):
    await message.reply_text(
                    text= helptext,
                    reply_markup = closebutton,
                    disable_web_page_preview = True)
                    

@bot.on_callback_query(filters.regex("startmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
    text = starttext.format(query.from_user.mention),
    reply_markup=startbutton,
    disable_web_page_preview=False
    )

@bot.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(
    text = helptext,
    reply_markup=backtohome,
    disable_web_page_preview=False
    )

@bot.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

bot.run()
