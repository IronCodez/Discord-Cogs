import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Successfully loaded the cog `{extension}`")

    @commands.command()
    @commands.is_owner()
    async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Successfully unloaded the cog `{extension}`")

    @commands.command()
    @commands.is_owner()
    async def reload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Successfully reloaded the cog `{extension}`")
    
def setup(bot):
  bot.add_cog(Admin(bot))
