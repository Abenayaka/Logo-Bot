from pyrogram import Client as bot
from pyrogram import filters
import os 
from PIL import Image, ImageDraw, ImageFont
import random

fontpath = "./resources/fonts/"
listfonts = os.listdir(fontpath)
imgpath ="./resources/images/"
listano = os.listdir(imgpath + "anime")

@bot.on_message(filters.command("animelogo"))
async def logomake(_, message):
    if len(message.command) < 2:
            return await message.reply_text("Please give a text")
    m = await message.reply_text("Creating Logo")
    text = message.text.split(None, 1)[1]
    img = Image.open(imgpath + "anime/" + (random.choice(listano)))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    font = ImageFont.truetype(fontpath + (random.choice(listfonts)),150)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="green")
    animelogo = "animelogo.png"
    img.save(animelogo, "png")
    await message.reply_photo(
                photo=f"animelogo.png",
                caption="Your logo was created.",
            )
    await m.delete()       
    if os.path.exists(animelogo):
            os.remove(animelogo)
