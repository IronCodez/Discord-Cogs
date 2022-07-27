import discord
from discord.ext import commands

client = discord.Client(command_prefix=None, intents=None)
TOKEN = "your_token_here"

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cog.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN))
