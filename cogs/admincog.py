import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Successfully loaded the cog `{extension}`")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Successfully unloaded the cog `{extension}`")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f":white_check_mark: Successfully reloaded the cog `{extension}`")
    
def setup(bot):
  bot.add_cog(Admin(bot))
