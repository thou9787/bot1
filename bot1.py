#導入Discord.py
import discord
import json
import redis

#client是我們與Discord連結的橋樑
client = discord.Client(intents=discord.Intents.all())
pyRedis = redis.StrictRedis(host='localhost', port=6379, db=0)

#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)

@client.event
#當有訊息時
async def on_message(message):
    if message.author == client.user:
         return
    if (message.content.lower().startswith('/items') and message.channel.name == '活動專區'):
        isSignIn = pyRedis.setnx(message.author.id, 1)
        if (isSignIn):
            await message.channel.send('簽到成功 ' + "<@&1018513072673009705>" + '執事出來發錢喔')
        else:
            await message.channel.send('你簽到過囉QQ')
    
with open('items.json', "r", encoding = "utf8") as file:
    data = json.load(file)
client.run(data['token']) #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面

#<@451446799127805983>