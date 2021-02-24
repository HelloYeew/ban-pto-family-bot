from check import *

# check requirement
check_library()

# import requirement
import discord
import datetime
import random
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

ban_list = read_file("ban_link_list.txt")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game('Banning...'))

# "https://www.youtube.com/watch?v=wXnG6VET-dw"
# "กูบอกไปยังไอพวกชาตินรก ไอสัสชิบหายมีควย มึงทำไปทำเหี้ยอะไร ทำเพื่ออะไร อยากให้คนนู้นคนนี้เขาถูกใจไปหมดเลยไอ้เหี้ย มึงดียังไงไอเหี้ยสัสมึงดีตรงไหนหรอมึงเจ๋งหรอไอเหี้ยส้นตีนไอสัส"

pto_complain = "https://www.youtube.com/watch?v=_AuqfTVs9oU"
daeng_complain = ["อ้าวมึงด่าแข่งกูหรอไอเหี้ย", "มึงทำไปทำเหี้ยอะไร", "ทำเพื่ออะไร", "เจ๋งหรอไอเหี้ย",
                  "ด่าใครอีก ด่ากูหรอไอเหี้ย", "ห้าวตีนหรอไอเหี้ย", "เป็นเหี้ยไรอีก",
                  "https://www.youtube.com/watch?v=wXnG6VET-dw"]


@bot.event
async def on_ready():
    print("Banned P'To Family as")
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    now = datetime.datetime.now()
    write_file("message_log.txt", f"---------\nStart at {now.strftime('%Y-%m-%d %H:%M:%S')}\n---------")


@bot.event
async def on_message(message):
    channel = message.channel
    if message.author.name == "Kasumi Personal":
        write = f"{message.author.display_name}(Username : {message.author.name}) to {message.channel} (Server : {message.guild.name}) at {message.created_at} UTC : {message.content} (Me)"
        print(write)
        write_file("message_log.txt", write)
        return
    elif message.guild.name == "Saint World":
        write = f"{message.author.display_name}(Username : {message.author.name}) to {message.channel} (Server : {message.guild.name}) at {message.created_at} UTC : {message.content} (Ignored)"
        print(write)
        write_file("message_log.txt", write)
        return
    else:
        # if message.content == "":
        #     write = f"{message.author.display_name} to {message.channel} ({message.guild.name}) at {message.created_at}: [{message.attachments}]"
        # else :
        write = f"{message.author.display_name}(Username : {message.author.name}) to {message.channel} (Server : {message.guild.name}) at {message.created_at} UTC : {message.content}"
        print(write)
        write_file("message_log.txt", write)
        if " " in message.content:
            text = message.content
            split_text = text.split(" ")
            text_to_read = ""
            for i in split_text:
                if "https://" in i:
                    text_to_read = i
                    continue
            if text_to_read in ban_list:
                await message.delete()
                await channel.send(pto_complain)
                write_file("ban_link_list.txt",text_to_read)
                write_file("new_link.txt", text_to_read)
            elif ("www.youtube.com" or "youtu.be") in text_to_read:
                if check_youtube(text_to_read) :
                    await message.delete()
                    await channel.send(pto_complain)
                    write_file("ban_link_list.txt", text_to_read)
                    write_file("new_link.txt", text_to_read)
        else:
            if message.content in ban_list:
                await message.delete()
                channel = message.channel
                await channel.send(pto_complain)
            elif ("www.youtube.com" or "youtu.be") in message.content:
                if check_youtube(message.content) :
                    await message.delete()
                    await channel.send(pto_complain)
                    write_file("ban_link_list.txt", message.content)
                    write_file("new_link.txt", message.content)
            elif check_revenge_keyword(message.content):
                import random
                random_int = random.randint(0, len(daeng_complain)-1)
                await channel.send(daeng_complain[random_int])
                if message.content not in read_file("revenge_keyword.txt"):
                    write_file("revenge_keyword.txt", message.content)
                    write_file("new_revenge_keyword.txt", message.content)
            elif check_only_keyword(message.content):
                await message.delete()
                await channel.send(pto_complain)
                if message.content not in ban_list:
                    write_file("ban_link_list.txt", message.content)
                    write_file("new_link.txt", message.content)

# @bot.command()
# async def profile(ctx):



bot.run(bot_token)
