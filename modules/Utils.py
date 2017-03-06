from discord.ext import commands
import discord


class Utils:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(':ping_pong: Pong !')


def setup(bot):
    bot.add_cog(Utils(bot))