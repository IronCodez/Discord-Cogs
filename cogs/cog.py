import discord
from discord.ext import commands

class cog(commands.Cog):

commands.is_owner()
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Successfully loaded the cog `{extension}`")

@commands.is_owner()
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Successfully unloaded the cog `{extension}`")
    
@commands.is_owner()
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Successfully reloaded the cog `{extension}`")
    
def setup(bot):
  bot.add_cog(examplecog(bot))
