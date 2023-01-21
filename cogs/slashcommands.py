import discord
from discord import app_commands
from discord.ext import commands

class botinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @app_commands.command(name="command_name", description=f"command description")
    async def command_name(self, interaction: discord.Interaction) -> None:
      interaction.send_message("This is an example of a slash (/) command in a cog.")
      
async def setup(client):
    await client.add_cog(botinfo(client))
