import discord
import random
from discord.ext import commands
from PIL import Image,ImageDraw
client = discord.Client()
bot=commands

def hp_calc(hp,total):
 val=(hp/total)*19
 r_val=int(val)
 return r_val

def hp_display(hp1,hp2,tot1,tot2):
    #val range between 1 to 19
    val1=hp_calc(hp1,tot1)
    if val1==0:
        val1+=1
    val2=hp_calc(hp2,tot2)
    if val2==0:
        val2+=1
    x1_org=5
    x1= x1_org + int((val1)-1)*12
    y1=285
    color1=(98,211,245)
    x2_org=362
    y2=293
    x2= x2_org + int((val2)-1)*12
    color2=(235,52,52)
    diam=12
    img=Image.open('progress.png').convert('RGB')
    draw=ImageDraw.Draw(img)
    #drawing 1st hp
    draw.ellipse([x1,y1,x1+diam,y1+diam], fill=color1)
    ImageDraw.floodfill(img, xy=(6,291), value=color1, thresh=40)
    text1=f" HP : {hp1}/ {tot1}"
    draw.text((34,286), text1,fill ="black")
    #drawing 2nd hp
    draw.ellipse([x2,y2,x2+diam,y2+diam], fill=color2)
    ImageDraw.floodfill(img, xy=(369,293), value=color2, thresh=40)
    text2=f" HP : {hp2}/ {tot2}"
    draw.text((406,293), text2,fill ="black")
    img.save('result.png')

async def create_embed(message,nam,hp1,hp2,tot1,tot2):
      cvalue = random.randint(0, 0xffffff)
      embed = discord.Embed(title=f" Dragon Kunj vs {nam} ", description="",color=cvalue)
      #embed.set_thumbnail(url=message.author.avatar_url)
      embed.add_field(name="Dragon Kunj  ", value=f"HP : {hp1} / {tot1} ", inline=True)
      hp_display(hp1,hp2,tot1,tot2)
      file= discord.File("result.png")
      embed.set_image(url="attachment://result.png")
      embed.add_field(name=f"{nam} ",value=f"HP:{hp2} / {tot2} ", inline=True)
      await message.channel.send(file=file,embed=embed)
