from EmiliaAnimeBot.events import register
from EmiliaAnimeBot import OWNER_ID
from EmiliaAnimeBot import telethn as tbot
import os
import random
from PIL import Image, ImageDraw, ImageFont


logopics = [
 
 "./EmiliaAnimeBot/resources/logopics/Logofile1.jpg",
	
 "./EmiliaAnimeBot/resources/logopics/LogoFile2.jpg",
	
 "./EmiliaAnimeBot/resources/logopics/Logofile3.jpg",
	
 "./EmiliaAnimeBot/resources/logopics/LogoFile4.jpg"
 
]

logofonts = [
 
 "./EmiliaAnimeBot/resources/logofonts/RemachineScriptPersonalUseOnly-yZL3.ttf",
	
 "./EmiliaAnimeBot/resources/logofonts/beyond-wonderland.regular.ttf",
	
 "./EmiliaAnimeBot/resources/logofonts/Respective-VP6y.ttf"
 
]


@register(pattern="^/logo ?(.*)")
async def lego(event):
 quew = event.pattern_match.group(1)
 if event.sender_id == OWNER_ID:
     pass
 else:

    if not quew:
       await event.reply('Provide Some Text To Draw!')
       return
    else:
       pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.pattern_match.group(1)
    img = Image.open(random.choice(logopics))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype(random.choice(logofonts) , 250)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="yellow", stroke_width=25, stroke_fill="black")
    fname2 = "Logo.png"
    img.save(fname2, "png")
    await tbot.send_file(event.chat_id, fname2, caption="Made By @EmiliaAnimeRoBot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @TangentChats, {e}')

   
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")


__mod_name__ = "Logos"

__help__ = """

`/logo` *:* Create a logo with text!

"""

