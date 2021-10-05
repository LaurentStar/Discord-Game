""""
Copyright © Krypton 2021 - https://github.com/kkrypt0nn
Description:
This is a template to create your own discord bot in python.

Version: 3.0
"""

import json
import os
import sys

import aiohttp
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import pandas as pd

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class GameTag(commands.Cog, name="game_tag"):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="inputCommand",
        description="Set a user command to be acted upon",
        guild_ids=[856227000259575819]
    )
    async def inputCommand(self, context: SlashContext):
        # This is, for now, only temporary
        with open("blacklist.json") as file:
            blacklist = json.load(file)
        if context.author.id in blacklist["ids"]:
            return

        df = pd.read_excel('tag_user_data.xlsx').set_index('Name')
        df[context.author.name]['current action'] = 'move'
        df.to_excel('tag_user_data.xlsx')

def setup(bot):
    bot.add_cog(GameTag(bot))
