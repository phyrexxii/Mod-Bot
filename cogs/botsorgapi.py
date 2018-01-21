import json
import aiohttp
import asyncio
import os
uri = 'https://discordbots.org/api'

class botsorgapi:
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def __unload(self):
        self.bot.loop.create_task(self.session.close())

    async def send(self):
        dump = json.dumps({
            'server_count': len(self.bot.servers)
        })
        head = {
            'authorization': os.environ.get('DBLT'),
            'content-type' : 'application/json'
        }

        url = '{0}/bots/399115688792424448/stats'.format(uri)

        async with self.session.post(url, data=dump, headers=head) as resp:
            print('returned {0.status} for {1}'.format(resp, dump))

    async def on_server_join(self, server):
        await self.send()

    async def on_server_remove(self, server):
        await self.send()

    async def on_ready(self):
        await self.send()
        
        
    
        

def setup(bot):
    bot.add_cog(botsorgapi(bot))
