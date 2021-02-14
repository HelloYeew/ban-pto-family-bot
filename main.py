from check import *

# check requirement
check_library()

# import requirement
import discord
from discord.ext import commands
from check_link import *
from function import *



# put all API key and bot token here

bot_token = 'bot_token'

# First Config

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# read ban file as list

ban_list = read_ban_file()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game('Banning...'))

# "https://www.youtube.com/watch?v=wXnG6VET-dw"
# "กูบอกไปยังไอพวกชาตินรก ไอสัสชิบหายมีควย มึงทำไปทำเหี้ยอะไร ทำเพื่ออะไร อยากให้คนนู้นคนนี้เขาถูกใจไปหมดเลยไอ้เหี้ย มึงดียังไงไอเหี้ยสัสมึงดีตรงไหนหรอมึงเจ๋งหรอไอเหี้ยส้นตีนไอสัส"

random_complain = "https://www.youtube.com/watch?v=wXnG6VET-dw"
daeng_complain = "อ้าวมึงด่าแข่งกูหรอไอเหี้ยชาตินรก"
ignore_message = ["กูบอกไปยังไอพวกชาตินรก ไอสัสชิบหายมีควย มึงทำไปทำเหี้ยอะไร ทำเพื่ออะไร อยากให้คนนู้นคนนี้เขาถูกใจไปหมดเลยไอ้เหี้ย มึงดียังไงไอเหี้ยสัสมึงดีตรงไหนหรอมึง เจ๋งหรอไอเหี้ย ส้นตีนไอสัส",
"อ้าวมึงด่าแข่งกูหรอไอเหี้ยชาตินรก"]

@bot.event
async def on_ready():
    print("Banned P'To Family as")
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    channel = message.channel
    if message.guild.name == "Saint World":
        print(f"{message.channel} ({message.guild.name}): {message.content} (Ignored)")
        return
    else:
        print(f"{message.channel} ({message.guild.name}) : {message.content}")
        if message.content in ignore_message:
            return
        elif " " in message.content:
            text = message.content
            split_text = text.split(" ")
            text_to_read = ""
            for i in split_text:
                if "https://" in i:
                    text_to_read = i
                    continue
            if text_to_read in ban_list:
                await message.delete()
                await channel.send(random_complain)
                write_file("ban_link_list.txt",text_to_read)
                write_file("new_link.txt", text_to_read)
            elif ("www.youtube.com" or "youtu.be") in text_to_read:
                if check_youtube(text_to_read) :
                    await message.delete()
                    await channel.send(random_complain)
                    write_file("ban_link_list.txt", text_to_read)
                    write_file("new_link.txt", text_to_read)
        else:
            if message.content in ban_list:
                await message.delete()
                channel = message.channel
                await channel.send(random_complain)
            elif ("www.youtube.com" or "youtu.be") in message.content:
                if check_youtube(message.content) :
                    await message.delete()
                    await channel.send(random_complain)
                    write_file("ban_link_list.txt", message.content)
                    write_file("new_link.txt", message.content)
            elif check_daeng_word(message.content):
                await channel.send(daeng_complain)
            elif check_only_keyword(message.content):
                await message.delete()
                await channel.send(random_complain)
                if message.content not in ban_list:
                    write_file("ban_link_list.txt", message.content)
                    write_file("new_link.txt", message.content)

# @bot.command()
# async def profile(ctx):



bot.run(bot_token)
