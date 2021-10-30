from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import Message
import os 
from PIL import Image, ImageDraw, ImageFont
import random

path1 = "./resources/images/"
img1 = os.listdir(path1)
background = path1 + '/' + (random.choice(img1))

@bot.on_message(filters.command("logo"))
async def logomake(_, message: Message):
    if len(message.command) < 2:
            return await message.reply_text("Please give a text")
    m = await message.reply_text("Creating Logo")
    text = message.text.split(None, 1)[1]
    img = Image.open(background)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    font = ImageFont.truetype("./resources/fonts/7thc.ttf",40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="yellow")
    logoname = "logo.png"
    img.save(logoname, "png")
    await message.reply_photo(
                photo=f"logo.png",
                caption="Your logo was created.",
            )
    await m.delete()       
    if os.path.exists(logoname):
            os.remove(logoname)   