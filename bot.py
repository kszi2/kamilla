import discord
import logger
import logging
import schpincer
from util import register

kamilla = discord.Bot()

debugLogger = logger.Logger(level=logging.DEBUG)
warningLogger = logger.Logger(level=logging.WARNING)

TOKEN = str(open("runtime/secret", "r").read())


def start():
    register([command_latency, command_opening])
    kamilla.run(TOKEN)


def command_latency():
    @kamilla.command(description="Tests basic behavior.")  # this decorator makes a slash command
    async def ping(ctx):  # a slash command will be created with the name "ping"
        await ctx.respond(f"Pong! Latency is {round(kamilla.latency * 1000, 1)}ms", ephemeral=True)
        debugLogger.log(f"{ctx.author=} used /ping")


def command_opening():
    @kamilla.command(description="Displays the current schpincér openings.")  # this decorator makes a slash command
    async def opening(ctx):  # a slash command will be created with the name "ping"
        openings = schpincer.parse(schpincer.fetch('https://schpincer.sch.bme.hu/api/items/now'))
        out = []
        for o in openings:
            out.append(str(o))
        await ctx.respond(f"{out}")
        debugLogger.log(f"{ctx.author=} used /opening")
