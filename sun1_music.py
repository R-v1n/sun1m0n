import discord
import sun1_func
import random
import youtube_dl
import asyncio
import os
from discord.ext import commands
import urllib.parse, urllib.request, re
client = discord.Client()
bot=commands

def del_song(track):
  if os.path.exists(track):
     os.remove(track)

def tr_search():
   a="track"
   b=".mp3"
   tr=a+b
   if not os.path.exists(tr):
       return a
   else :
        i=1
        while os.path.exists(tr):
            y=a+str(i)
            tr=y+b
            i+=1
        return y


def yt_search(search,ans):
        flag=ans
        query_string = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query_string)
        search_results = re.findall(r'/watch\?v=(.{11})',
                                    htm_content.read().decode())
        if flag==0:
            x='http://www.youtube.com/watch?v=' + search_results[0]
            return x
        else:
            x=[]
            for i in range(int(ans)):
               x.append('http://www.youtube.com/watch?v=' + search_results[i])
            return x
async def res_send(res,message,ans):
   for i in range(int(ans)):
     await message.channel.send(f" search result : {int(i)+1} ")
     await message.channel.send(res[i])

def track_name():
    x=path
    return x

@bot.command(name='music')
async def playmusic(vc, url,message,song):
        track=tr_search()
        ip_addr='0.0.0.0'
        ydl_opts = {
            'outtmpl': f'{track}.%(ext)s',
            'format': 'bestaudio/best',
            'source_address':f"{ip_addr}",
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '360',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         try:
             file = ydl.extract_info(url, download=True)
         except:
              await message.channel.send("error playing music ..please try again later ")
              await vc.disconnect()
         global path
         path=f"{track}.mp3"
         await message.channel.send(f"playing {song}..venamengil ketto")
         vc.play(discord.FFmpegPCMAudio(path), after=lambda e:del_song(path))
         vc.source = discord.PCMVolumeTransformer(vc.source, 1)

         while vc.is_playing():
             await asyncio.sleep(1)
         if not vc.is_paused():
          vc.stop()
          await vc.disconnect()
