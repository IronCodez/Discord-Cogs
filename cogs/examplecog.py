import discord
from discord.ext import commands

class examplecog(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #Example of an event in a cog.
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
      print("This is an example of an event in a cog!")
      
    #Example of a command in a cog.
    @commands.command()
    async def command(self, ctx):
        await ctx.send("This is an example of a command in a cog!")
      
async def setup(client):
    await client.add_cog(examplecog(client))
