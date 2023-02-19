import discord
from secretTokens import TOKEN
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = commands.Bot(command_prefix="!", intents = intents)

# Channel names for potential channels that CluBot is scraping
CHANNEL_LIST = []

@client.event
async def on_ready():
    print("---------------------------------------------")
    print('We have logged in as {0.user}'.format(client))
    print("---------------------------------------------")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0] == "!":
        await client.process_commands(message)
        return
    
    print("message thing:")
    print(message.content)
    print("\n")

@client.command()
async def shutdown(ctx):
    print("---------------------------------------------")
    print("Shutting down Clubot")
    print("---------------------------------------------")
    await ctx.bot.close()

@client.command()
async def msg(ctx, user:discord.Member, *, message=None):
    message = "Rohits a bitch"
    embed = discord.Embed(title=message)
    await user.send(embed=embed)
    
client.run(TOKEN)
