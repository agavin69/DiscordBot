#DiscordBot



# import discord

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

# intents = discord.Intents.default()
# intents.message_content = True

# client = MyClient(intents=intents)
# client.run('my token goes here')


import discord
from discord.ext import commands
import DOTA_REQUESTS






intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def test(ctx):
    await ctx.send('FuckGuwop')


@bot.command()
async def mathadd(ctx, x: float, y: float):
    await ctx.send(x + y)

@bot.command()
async def mathmult(ctx, x: float , y: float):
    await ctx.send( x * y)





# client.run('MTAyMjU4NDc2NjMzNzQwMDg0Mw.GNEJRO.oLCC7U7AKkfYZz9gSLrFamx2tHJDU0l6EpooHc')
bot.run('MTAyMjU4NDc2NjMzNzQwMDg0Mw.GNEJRO.oLCC7U7AKkfYZz9gSLrFamx2tHJDU0l6EpooHc')