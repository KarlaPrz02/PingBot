import discord
from discord.ext import commands

USER1_ID = USER1
USER2_ID = USER2

# intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  
intents.presences = True  

bot = commands.Bot(command_prefix="!", intents=intents)

# Slash command 
@bot.event
async def on_ready():
    print(f"Connected as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"Error sync commands: {e}")
        
    activity = discord.Activity(type=discord.ActivityType.watching, name="WHATEVER U WANT")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.tree.command(name="WHATEVER U WANT", description="DESCRIPTION OF THE COMMAND")
async def juni_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f"<@{USER1_ID}> <@{USER2_ID}>")

@bot.command(name="juni")
async def juni_prefix(ctx):
    await ctx.send(f"<@{USER1_ID}> <@{USER2_ID}>")

bot.run("BOT_TOKEN")
