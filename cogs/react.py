import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json','r',encoding='utf8') as jfile:
   jdata = json.load(jfile)

class react(Cog_Extension):
    #用於偵測你講出的話後面是否包含偵測中的字詞
    @commands.Cog.listener()
    async def on_message(selF,msg):
        if msg.content.endswith('好甲喔'):
            gay = jdata['gay']
            await msg.channel.send(gay) 

        if msg.content.endswith('初吻'):
            dioda = jdata['dioda']
            await msg.channel.send(dioda)

        if msg.content.endswith('共匪'):
            共匪 = jdata['共匪']
            await msg.channel.send(共匪)

        if msg.content.endswith('龍舌蘭酒'):
            龍舌蘭酒 = jdata['龍舌蘭酒']
            await msg.channel.send(龍舌蘭酒)

        if msg.content.endswith('說謊的味道'):
            說謊的味道 = jdata['說謊的味道']
            await msg.channel.send(說謊的味道)

        if msg.content.endswith('我不做人啦'):
            我不做人啦 = jdata['我不做人啦']
            await msg.channel.send(我不做人啦)

        if msg.content.endswith('典明粥'):
            典明粥 = jdata['典明粥']
            await msg.channel.send(典明粥)

        if msg.content.endswith('阿帕茶'):
            阿帕茶 = jdata['阿帕茶']
            await msg.channel.send(阿帕茶)

        if msg.content.endswith('喝'):
            喝 = jdata['喝']
            await msg.channel.send(喝)

        if msg.content.endswith('勃起'):
            boki = jdata['boki']
            await msg.channel.send(boki)

        if msg.content.endswith('救護車'):
            jo護車 = jdata['jo護車']
            await msg.channel.send(jo護車)

        if msg.content.endswith('塞車'):
            塞車 = jdata['塞車']
            await msg.channel.send(塞車)

        if msg.content.endswith('沒用'):
            沒用 = jdata['沒用']
            await msg.channel.send(沒用)

        if msg.content.endswith('yes'):
            joyes = jdata['joyes']
            await msg.channel.send(joyes)

        if msg.content.endswith('no'):
            jono = jdata['jono']
            await msg.channel.send(jono)

        if msg.content.endswith('是我啦'):
            dioda = jdata['dioda']
            await msg.channel.send(dioda)

        if msg.content.endswith('high到不行'):
            high到不行 = jdata['high到不行']
            await msg.channel.send(high到不行)

        if msg.content.endswith('替身攻擊'):
            替身攻擊 = jdata['替身攻擊']
            await msg.channel.send(替身攻擊)

        if msg.content.endswith('想想辦法啊'):
            想想辦法啊 = jdata['想想辦法啊']
            await msg.channel.send(想想辦法啊)

        if msg.content.endswith('西薩'):
            西薩 = jdata['西薩']
            await msg.channel.send(西薩)

        if msg.content.endswith('壓路機'):
            壓路機 = jdata['壓路機']
            await msg.channel.send(壓路機)

        if msg.content.endswith('wryyy'):
            wryyy = jdata['wryyy']
            await msg.channel.send(wryyy)

        if msg.content.endswith('櫻桃'):
            櫻桃 = jdata['櫻桃']
            await msg.channel.send(櫻桃)

        if msg.content.endswith('最後的波紋'):
            最後的波紋 = jdata['最後的波紋']
            await msg.channel.send(最後的波紋)

        if msg.content.endswith('我拒絕'):
            我拒絕 = jdata['我拒絕']
            await msg.channel.send(我拒絕)

        if msg.content.endswith('呦喜'):
            呦喜 = jdata['呦喜']
            await msg.channel.send(呦喜)

        if msg.content.endswith('你下一句話要說的是'):
            你下一句話要說的是 = jdata['你下一句話要說的是']
            await msg.channel.send(你下一句話要說的是)

        if msg.content.endswith('德意志科技世界第一'):
            德意志科技世界第一 = jdata['德意志科技世界第一']
            await msg.channel.send(德意志科技世界第一)

        if msg.content.endswith('玩腿'):
            玩腿 = jdata['玩腿']
            await msg.channel.send(玩腿)

        if msg.content.endswith('nice'):
            nice = jdata['nice']
            await msg.channel.send(nice)

        if msg.content.endswith('成為超棒的單親媽媽的'):
            單親媽 = jdata['單親媽']
            await msg.channel.send(單親媽)

        if msg.content.endswith('很戲劇化的發展嗎'):
            戲劇化 = jdata['戲劇化']
            await msg.channel.send(戲劇化)

        if msg.content.endswith('感情問題'):
            感情問題 = jdata['感情問題']
            await msg.channel.send(感情問題)

        if msg.content.endswith('令人驚豔'):
            令人驚豔 = jdata['令人驚豔']
            await msg.channel.send(令人驚豔)

async def setup(bot):
    await bot.add_cog(react(bot))