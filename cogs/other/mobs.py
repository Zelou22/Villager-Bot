from discord.ext import commands
import discord
import random
import math


class Mobs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.d = self.bot.d

        self.db = self.bot.get_cog('Database')

        self.bot.loop.create_task(self.spawn_events())

    async def calc_sword_damage(self, uid, sword, diff_multi):
        sword = sword.lower()

        if sword == 'netherite sword':
            dmg = random.randint(7, 10)
        elif sword == 'diamond sword':
            dmg = random.randint(6, 7)
        elif sword == 'gold sword':
            dmg = random.randint(4, 5)
        elif sword == 'iron sword':
            dmg = random.randint(2, 4)
        elif sword == 'stone sword':
            dmg = random.randint(1, 3)
        else:
            dmg = randint(1, 2)

        if diff_multi > 1:
            dmg = dmg / 1.3

        if await self.db.fetch_item(uid, 'Sharpness II Book') is not None:
            dmg *= 1.5
        elif await self.db.fetch_item(uid, 'Sharpness I Book') is not None:
            dmg *= 1.25

        return math.ceil(dmg)

    async def spawn_event(self, ctx):
        pass

    async def spawn_events(self):
        while True:
            await asyncio.sleep(.05)  # don't fucking remove this or else
            for ctx in self.d.spawn_queue:
                self.bot.loop.create_task(self.spawn_event(ctx))

def setup(bot):
    bot.add_cog(Mobs(bot))