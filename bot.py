import discord
import sun1_func
import urllib.parse, urllib.request, re
import random
from discord.ext import commands
client = discord.Client()
bot=commands
import sun1_music
import drag_mini
global v_c

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
aflag=0
sun1_func.init_prev()
def assign_no():
  flag=1
  y=str(random.randint(1,9))
  num=y
  for i in range(3):
       while flag==1:
         x=str(random.randint(1,9))
         y=num
         if x in y:
             flag=1
         else :
            flag=0

       num=num+x
       flag=1
       snum=num
  return snum

def check_no(num):
    flag=0
    if len(num)==4:
     for i in range(4):
        for j in range(4):
            if i!=j:
                if num[i]==num[j]:
                    flag=1

     for i in range(4):
      if num[i]=='0':
       flag=1
    else:
        flag=2
    return flag

def c_and_b(num1,num2):
 b=0
 c=0
 for i in range(4):
     for j in range(4):
         if i==j:
             if num1[i]==num2[j]:
                 b+=1
         elif i!=j:
          if num1[i]==num2[j]:
              c+=1
 rnum=[]
 rnum.append(b)
 rnum.append(c)
 return rnum

async def s_candb(message):
 num1=assign_no()
 channel=message.channel
 user=message.author
 def check(m):
   return user == m.author and channel==m.channel
 await channel.send(" help: ente secret no ningal kandupidikkanam.. \n c: digit in the required no   b: digit in same place ")
 await channel.send('please enter the number of tries .maximum:6')
 msg = await client.wait_for('message',check=check,timeout=60)
 x=msg.content
 if int(x)>6:
     await channel.send('sun1_m0nee pattikan nokkale')
     return
 else:
     for i in range(int(msg.content)):
        await channel.send('enter a non 0 and non repeating 4 dgit number (timeout : 90 sec).. command /sur to surrender')
        y="/sur"
        surrender=0
        msg = await client.wait_for('message',check=check,timeout=90)
        if not msg.content.lower().startswith(y):
            num2=msg.content
            flag=1
            while flag==1:
              if num2.isdigit():
               x= check_no(num2)
              else :
               x==2
              if x==0:
                 flag=0
              elif x==1:
                res="you entered a repeating number  or a number with 0..poyi valla vazhayum nadu \n enter a 4 digit number or /sur to surrender"
              elif x==2:
                 res="you didn't enter 4 digit number ..neeyokee thinnan vendi mathram janichatha.. \n enter a 4 digit number or /sur to surrender"
              if flag==1:
                 await channel.send(res)
                 msg = await client.wait_for('message',check=check,timeout=60)
                 if not msg.content.lower().startswith(y):
                     num2=msg.content
                 else :
                  flag=0
                  surrender=1
            if surrender==0:
             cb=c_and_b(num1,num2)
             bull=cb[0]
             cow=cb[1]
             if bull==4:
              await channel.send(f"jayichu... ithuthanneyanu number  {num1}")
              return
             await channel.send(f"its {bull} b and {cow} c")
            else :
                 await channel.send("thoottu pinmari alle..")
                 return
        else:
         await channel.send("thoottu pinmari alle..")
         return
     await channel.send(f"{user}  ...Nee thottu. ente number  {num1}")
y1="sunimon"
y2="sun1_m0n"
y3="sun1_mon"
y4="sun1mon"

@client.event
async def member_join(member):
    level.rank_def(member)
    for channel in member.guild.channels:
     if str(channel) == "general":
        await channel.send(f" Welcome to the server {member.name}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('s/help'):
       await sun1_func.bot_info(message)

    if message.content.lower().startswith('s/admin/exit'):
      quit()

    if message.content.lower().startswith('s/yts'):
        inp=message.content
        if inp=="s/yts":
         await message.channel.send(" please enter the search term..poyi valla Closetilum thala yiddeda monNesh")
        else :
          search=inp.replace("s/yts ","")
          await message.channel.send("please enter the number of results ( max : 5 )")
          def check(m):
            return m.author==message.author and m.channel == message.channel
          msg = await client.wait_for('message',check=check,timeout=60)
          ans=msg.content
          if(0<int(ans)<=5):
             y=sun1_music.yt_search(search,ans)
             await sun1_music.res_send(y,message,ans)
          else:
                await message.channel.send(" invalid choice ")


    if message.content.lower().startswith('s/candb'):
      await s_candb(message)
    if y1 in message.content or y2 in message.content or y3 in message.content or y4 in message.content:
       y=random.randint(1,3)
       if y==2:
        x= sun1_func.suni()
        await message.channel.send(x)
    if message.content.lower().startswith('s/sunipic'):
       await message.channel.send(file=discord.File("sunimon.png"))
    if message.content.lower().startswith('s/cflip'):
        channel=message.channel
        await channel.send('heads or tails')
        def check(m):
          return m.content=='heads' or m.content=='tails' and m.channel == channel

        msg = await client.wait_for('message', check=check,timeout=60)
        x=msg.content
        nam=message.author.name
        y=random.randint(1,2)
        if y==1:
           outc="heads"
        elif y==2:
           outc="tails"
        if x == outc :
          await message.channel.send(f'mwone {nam} ... {x} aada')
        elif x!=outc :
          oc=outc
          await message.channel.send(f'mwone {nam} ...{oc} aanu..vechitt poodai')

    if  message.content.lower().startswith('s/play') or message.content.lower().startswith('s/pause') or message.content.lower().startswith('s/stop') or message.content.lower().startswith('s/resume'):
        connected = message.author.voice
        if connected:
          channel=message.channel
          msg = message.content
          x=msg
          v_cl=connected.channel
          botv= message.guild.voice_client
          if not botv:
            v_c=await v_cl.connect()
          else :
            v_c=botv
          if x.lower().startswith('s/play'):
            if x=="s/play":
              await message.channel.send("please specify track name.. pattinte peeru parayada..*$#")
              await v_c.disconnect()
            else:
                if v_c.is_paused():
                 await message.channel.send("a song is currently paused. u can resume it or stop it to play next song..(engane undu ente engislh..)")
                else:
                 if not v_c.is_playing():
                  search=x.replace("s/play ","")
                  key=" song ,lyrical "
                  s_key=search+key
                  y=sun1_music.yt_search(s_key,0)
                  await sun1_music.playmusic(v_c,y,message,search)
                 else :
                     await message.channel.send("a song is currently playing.please use the s/stop command to stop song ..")
                     await message.channel.send(" subtitle: Aadyam paatu nirthedaa..manda..")
          elif  x.lower().startswith('s/pause'):
            if v_c.is_playing():
                await message.channel.send("karayanda..pause cheythittundu")
                v_c.pause()
          elif  x.lower().startswith('s/resume'):
            if v_c.is_paused():
               await message.channel.send("ippo sheriyakki tharam..")
               v_c.resume()
          elif  x.lower().startswith('s/stop'):
              await message.channel.send("nirthee ..nyan pattu nirthee")
              v_c.stop()
              await v_c.disconnect()
        else:
         await message.channel.send(str(message.author.name) + "  is not in a channel.")


    if message.content.lower().startswith('s/dr') :
        def all_move(self,user):
            flag=1
            x=self.attack
            ct=0
            for i in range(1,4):
             y="a"+str(i)
             if x[y]["mov_no"]==0:
                  ct+=1
            if ct==3:
               flag=0
               return flag
            x=user.attack
            ct=0
            for i in range(1,4):
             y="a"+str(i)
             if x[y]["mov_no"]==0:
                  ct+=1
            if ct==3:
               flag=0
               return flag
            return flag

        def attack_acc(x):
         y=random.randint(1,100)
         if y>=x:
             return 0
         else :
             return 1

        async def hp_disp(drhp,ushp,dr_tot,us_tot,uname,message):
            hp1=drhp
            tot1=dr_tot
            hp2=ushp
            tot2=us_tot
            await drag_mini.create_embed(message,uname,hp1,hp2,tot1,tot2)

        def mov_check(att):
         if att["mov_no"]==0:
             return 0

        class user():
            def __init__(self,x):
                self.name=x
                self.lv=random.randint(1,4)
                self.tot_hp=1200*3+100*self.lv
                self.hp=self.tot_hp
                self.attack= {
                              "a1":{"a_name":"vedi vechu","damage":400,"accuracy":95,"mov_no":20},
                              "a2":{"a_name":"Pst 120 brutal 180 MS ","damage":1000,"accuracy":65,"mov_no":5},
                              "a3":{"a_name":"COvid 20","damage":750,"accuracy":85,"mov_no":10}
                            }
            async def display_attack(self):
                us_att=self.attack
                m1=us_att["a1"]["mov_no"]
                m2=us_att["a2"]["mov_no"]
                m3=us_att["a3"]["mov_no"]
                """
                 att_no          att_name                  damage                   accuracy          no_of_mov
                 1>              vedi vechu                400                        95                 {m1}
                 2>              Pst 120 brutal 180 MS     1000                       65                 {m2}
                 3>              COvid 20                  750                        85                 {m3}
                """
                cvalue = random.randint(0, 0xffffff)
                embed = discord.Embed(title=" Select A move ", description=" enter move.no <1,2,3> or enter /sur to surrender ",color=cvalue)
                embed.add_field(name="att_name : ", value="<< (1) vedi vechu >><< (2) Pst 120 brutal 180 MS >><< (3) COvid 20 >>", inline=False)
                embed.add_field(name="damage : ",value="<< (1) 400 >><< (2) 1000 >><< (3) 750 >>", inline=False)
                embed.add_field(name="accuracy : ",value="<< (1) 95 >><< (2) 65 >><< (3) 85 >>", inline=False)
                embed.add_field(name="no of mov: ",value=f"<< (1) {m1} >><< (2) {m2} >><< (3) {m3} >>", inline=False)
                await message.channel.send(embed=embed)


        class dragon():
         def __init__(self):
            self.name="dragon kunju"
            self.lv=random.randint(5,10)
            self.tot_hp=1000*3+100*self.lv
            self.hp=self.tot_hp
            self.attack={
                          "a1": {"a_name":"thee thuppi","damage":450,"accuracy":90 ,"mov_no":20},
                          "a2":{"a_name":"Kadich keeri","damage":1150,"accuracy":65,"mov_no":5},
                          "a3":{"a_name":"Dragon Dinner","damage":750,"accuracy":85,"mov_no":10}
                        }
         async  def battle(self,user,message):
             msc=message.channel
             rep=f"""oh..Munthiya enam {self.name} appeared ...
                     what do u wish to do?
                     1>fight 2>flee 3>flee 4>fleee   """
             await msc.send(rep)
             def check(m):
               return m.author==message.author and m.channel == message.channel
             msg = await client.wait_for('message',check=check,timeout=60)
             ans=msg.content
             ch=int(ans)
             while not (ch==1 or ch==2 or ch==3 or ch==4) :
                 await msc.send("invalid choice or enter /sur to surrender")
                 msg = await client.wait_for('message',check=check,timeout=60)
                 ans=msg.content
                 ch=int(ans)
             if ch==1:
                 flag=0
                 init=0
                 a_hp=self.hp
                 b_hp=user.hp
                 atot=self.tot_hp
                 btot=user.tot_hp
                 b_name=user.name
                 await hp_disp(a_hp,b_hp,atot,btot,b_name,message)
                 y=random.randint(1,2)
                 mv=0
                 a_prev=0
                 while flag==0:
                     if all_move(self,user)==0:
                         x="""there is no move left ...
                              ......exiting......"""
                         await msc.send(x)
                         return
                     if y==1:
                      mv+=1
                      init+=1
                      await user.display_attack()
                      def check(m):
                        return m.author==message.author and m.channel == message.channel
                      msg = await client.wait_for('message',check=check,timeout=180)
                      ans=msg.content.lower()
                      if ans=="/sur":
                         await msc.send("Dragon kunj parannu poyi..")
                         return
                      ansi=int(ans)
                      while not (ansi==1 or ansi==2 or ansi==3) :
                          await msc.send("invalid choice or enter /sur to surrender")
                          msg = await client.wait_for('message',check=check,timeout=180)
                          ans=msg.content.lower()
                          if ans=="/sur":
                              await msc.send("Dragon kunj parannu poyi..")
                              return
                          ansi=int(ans)
                      y="a"+str(ansi)
                      att=user.attack[y]
                      while mov_check(att)==0:
                        await msc.send("the number of available move is zero .please select another move.. ")
                        msc.send("enter the move number : or enter /sur to surrender ")
                        def check(m):
                          return m.author==message.author and m.channel == message.channel
                        msg = await client.wait_for('message',check=check,timeout=180)
                        ans=msg.content.lower()
                        if ans=="/sur":
                           await msc.send("Dragon kunj parannu poyi..")
                           return
                        ch=int(ans)
                        while not (ch==1 or ch==2 or ch==3) :
                            await msc.send("invalid choice or enter /sur to surrender")
                            msg = await client.wait_for('message',check=check,timeout=180)
                            ans=msg.content.lower()
                            if ans=="s/sur":
                                await msc.send("Dragon kunj parannu poyi..")
                                return
                            ch=int(ans)

                        y="a"+str(ch)
                        att=user.attack[y]
                      acc=att["accuracy"]
                      aname=att["a_name"]
                      user.attack[y]["mov_no"]-=1
                      await msc.send(f"{user.name} used {aname} ...\n")
                      hit=attack_acc(acc)
                      if hit==1:
                          if aname == "Pst 120 brutal 180 MS":
                              if a_prev<2:
                                  a_prev+=1
                          else:
                                if a_prev>0:
                                    a_prev=0
                          dmg=att["damage"]
                          self.hp-=dmg
                          await msc.send(f"""{user.name}'s  {aname} did a damage of : {dmg}""")
                      else:
                         await msc.send("Dragon kunj evaded the attack..neere nokki viddu_")
                      if not self.hp<=0:
                        y=2
                      else:
                          flag=1
                          break
                     if mv==2:
                          y=random.randint(1,2)
                     if  init==2:
                      a_hp=self.hp
                      b_hp=user.hp
                      b_name=user.name
                      atot=self.tot_hp
                      btot=user.tot_hp
                      b_name=user.name
                      await hp_disp(a_hp,b_hp,atot,btot,b_name,message)
                      init=0

                     if y==2:
                        mv+=1
                        init+=1
                        x=random.randint(1,3)
                        a_nam="a"+str(x)
                        att=self.attack[a_nam]
                        while mov_check(att)==0:
                          x=random.randint(1,3)
                          a_nam="a"+str(x)
                        acc=att["accuracy"]
                        aname=att["a_name"]
                        self.attack[a_nam]["mov_no"]-=1
                        await msc.send(f" Dragon kunj used {aname} ")
                        hit=attack_acc(acc)
                        if hit==1:
                            if not(aname=="thee thuppi" and a_prev==2):
                               dmg=att["damage"]
                               user.hp-=dmg
                               await msc.send(f""" Dragon Kunj's  {aname} did a damage of : {dmg} """)
                            else :
                               await msc.send("Dragon kunj..too much Brutal 120 MS..Unable to use thee thuppi ..")
                        else:
                            await msc.send(f"{user.name} evaded the attack..")
                        if not user.hp<=0:
                          y=2
                        else:
                            flag=1
                            break
                        y=1
                     if mv==2:
                         y=random.randint(1,2)
                         mv=0
                     if  init==2:
                      a_hp=self.hp
                      b_hp=user.hp
                      b_name=user.name
                      atot=self.tot_hp
                      btot=user.tot_hp
                      b_name=user.name
                      await hp_disp(a_hp,b_hp,atot,btot,b_name,message)
                      init=0
                 if self.hp<=0:
                     mess=f"""----------------------------------
                          dragon kunj fainted..
                          {user.name}  dragon kunjinee konnn..
                      """
                     await msc.send(mess)
                 elif user.hp<=0:
                    await msc.send(f"Dragon kunj  {user.name}_ne Konn ")
             elif ch==2 or ch==3 or ch==4 :
                 await msc.send(f"{user.name} kandam vazhi oodi...")

        async def drag_game(x,message):
            dr=dragon()
            u1=user(x)
            await dr.battle(u1,message)

        x=message.author.name
        await drag_game(x,message)

bot_code="enter your bot code"
client.run(bot_code)
