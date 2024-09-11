import datetime
import discord
import logger
import logging
import schpincer
from util import register
from discord import EmbedField

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
        reply = discord.Embed(title="Pong!",
                              description=f"Latency is {int(round(kamilla.latency * 1000, 0))}ms.",
                              color=0xffccee)
        await ctx.respond(embed=reply, ephemeral=True)
        debugLogger.log(f"{ctx.author=} used /ping")


def command_opening():
    @kamilla.command(description="Displays the current SchWaiter openings.")  # this decorator makes a slash command
    async def opening(ctx):  # a slash command will be created with the name "ping"
        openings = schpincer.parse(schpincer.fetch('https://schpincer.sch.bme.hu/api/items/now'))

        fields = []
        for o in openings:
            fields.append(EmbedField(name=o.__dict__.get("circleName") + " :green_circle:",
                                     value=f"{o.__dict__.get("nextOpeningDate")}"))
            fields.append(EmbedField(name="", value=""))

        reply = discord.Embed(title="🍴 Openings",
                              fields=fields,
                              color=0xffccee,
                              url="https://schpincer.sch.bme.hu/",
                              timestamp=datetime.datetime.now()
                              )

        if len(openings) == 0:
            reply.fields = [EmbedField(name="No Openings at the moment :cry:", value="")]

        await ctx.respond(embed=reply)
        debugLogger.log(f"{ctx.author=} used /opening")
