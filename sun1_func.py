import discord
import random
from discord.ext import commands
client = discord.Client()
bot=commands

async def bot_info(message):
    cvalue = random.randint(0, 0xffffff)
    embed = discord.Embed(title=" HELP ", description=" hello nyan Sun1_m0n.Available commands are :",color=cvalue)
    embed.add_field(name="s/sunipic",value="send sun1_m0n pic", inline=False)
    embed.add_field(name="s/cflip",value="coin flip", inline=False)
    embed.add_field(name="s/candb",value="play cows and bulls", inline=False)
    embed.add_field(name="s/play {track name}",value="play song", inline=False)
    embed.add_field(name="s/pause",value="pause song", inline=False)
    embed.add_field(name="s/resume",value="resume song", inline=False)
    embed.add_field(name="s/stop",value="stop song", inline=False)
    embed.add_field(name="s/dr",value="Dragon Kunj mini game", inline=False)
    embed.add_field(name="s/yts {search term }",value="search yt vid", inline=False)
    await message.channel.send(embed=embed)


def init_prev():
    global prev
    prev=[]
    global prev1
    prev1=[]

def prev_check(x):
    flag=0
    for key in prev:
        if x==key:
            flag=1
    return flag

def prev1_check(x):
    flag=0
    for key in prev1:
        if x==key:
            flag=1
    return flag

def prev_add(x):
    i=len(prev)
    if i>=30:
        prev.clear()
        prev.append(x)
    elif i<30:
      prev.append(x)
def th():
   x=random.randint(1,67)
   while prev_check(x)==1:
      x=random.randint(1,67)
   key=str(x)
   f=open("th.txt","r")
   for i in f:
     word=i
     if key in word :
        reply=word
        break
   f.close()
   prev_add(key)
   th_word=reply.replace(key,"")
   return th_word


async def cflip(message):
 channel=message.channel
 await channel.send('heads or tails')
 def check(m):
   return m.content.startswith('heads') or m.content.startswith('tails')  and m.channel == channel

 msg = await client.wait_for('message', check=check)
 x=msg.content
 return x



def suni():
  x=random.randint(1,10)
  while prev1_check(x)==1:
    x=random.randint(1,10)
  key=str(x)
  f=open("suni.txt","r")
  for i in f:
    word=i
    if key in word :
       reply=word
       break
  f.close()
  if len(prev1)>=3:
    prev1.clear()
    prev1.append(key)
  else:
    prev1.append(key)

  s_word=reply.replace(key,"")
  return s_word
