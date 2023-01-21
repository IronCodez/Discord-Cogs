import discord
from discord.ext import commands

class owner(commands.Cog):
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

async def setup(bot):
    await bot.add_cog(owner(bot))
