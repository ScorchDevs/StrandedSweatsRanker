from Main import *


@bot.command()
async def ping(ctx, arg):
    await ctx.send(arg)