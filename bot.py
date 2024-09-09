import discord
import logger
import logging

kamilla = discord.Bot()

debugLogger = logger.Logger(level=logging.DEBUG)
warningLogger = logger.Logger(level=logging.WARNING)

TOKEN = str(open("runtime/secret", "r").read())


def start():
    command_latency()
    kamilla.run(TOKEN)


def command_latency():
    @kamilla.command(description="Tests basic behavior.")  # this decorator makes a slash command
    async def ping(ctx):  # a slash command will be created with the name "ping"
        await ctx.respond(f"Pong! Latency is {round(kamilla.latency * 1000, 1)}ms", ephemeral=True)
        await debugLogger.log(f"{ctx.author=} used /ping")
