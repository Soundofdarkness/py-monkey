import discord
import logging
import sys
from discord.ext import commands
import config


"""Creating Basic Discord Logger
File Logger is activated , StreamLogger can get activated for debug purposes"""
discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.DEBUG)
#dStreamHandler = logging.StreamHandler(stream=sys.stdout)
dFileHandler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
dFormatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
#dStreamHandler.setFormatter(dformatter)
dFileHandler.setFormatter(dFormatter)
#discord_logger.addHandler(dStreamHandler)
discord_logger.addHandler(dFileHandler)


bot = commands.Bot(command_prefix=config.prefix, description=config.description, pm_help=True)


@bot.event
async def on_ready():
    print('CM Bot v1.0')
    print('----------------------')
    print('Username: ' + bot.user.name)
    print('ID: ' + str(bot.user.id))
    print('----------------------')

# No on_message event yet , as there is nothing which needs an external message handler yet

if __name__ == '__main__':

    # basic Extension loading based on commands.ext
    for ext in config.modules:
        try:
            bot.load_extension(ext)
            print('Sucessfully loaded: ' + ext)
        except Exception as e:
            print('Failed to load Extension {} due to \n {}'.format(ext, type(e).__name__))

    bot.run(config.token)