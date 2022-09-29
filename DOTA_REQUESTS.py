#DOTA REQUESTS


import discord
from discord.ext import commands
import requests
import json
import pandas as pd




class Dota_Info():


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def GavGodDota(self,ctx):

        request_url = 'https://api.opendota.com/api/players/837273849'

        r = requests.get(request_url)

        if r.status_code == 200:

            data = json.loads(r.text)
            df = pd.DataFrame(data)
            df.head(10)
            print(data)

            print(df)

