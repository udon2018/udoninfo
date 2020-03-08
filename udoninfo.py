#coding:utf-8
#!/usr/bin/env python3

import discord
from enum import Enum
from time import sleep

client = discord.Client()
text_channel = 315744357049303042 #じぇねらるのテキストチャンネルID
my_id = 315453873286545410
token = "token" #テスト1bot
owner = discord.User(id=my_id)

@client.event
async def on_ready():
    global text_chat
    text_chat = client.get_channel(text_channel)
    print ('logged in as')
    print (client.user.name)
    print (client.user.id)
    print ('------')
    await client.change_presence(activity=discord.Game("うどん情報網"))

@client.event
async def on_member_join(member):
    nk = "「読んでねチャンネル」の一番下に、通常閲覧権限追加の為のキーワードがあるので、確認の上「認証用チャンネル」に書き込みください"
    await member.send(nk)

@client.event
async def on_server_update(before,after):
    if before.region != after.region:
        msg = "サーバーリージョンが" + before.region + "から" + after.region + "に変更されました"
        chat_channel = client.get_channel(text_channel)
        await chat_channel.send(msg)

@client.event
async def on_message(message):
    if message.content.startswith('!うどんください'): #役職の合言葉
    role = discord.utils.get(message.author.guild.roles, name="メンバー")  #メッセージの主のの役職に移動先の役職を与える
    t_channel = client.get_channel('532073311329583106')
    mg = "認証中・・・"
    await t_channel.send(mg)
    sleep(5)
    await message.author.add_roles(message.author, role)
    mh = "役職の付与を行いました。"
    await client.send_message(message.author, mh)
    sleep(1)
    mr = message.author.name + "さんが役職変更されました"
    await guild.owner.send(owner, mr)
client.run(token)
