from Main import *

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}')
    channel = bot.get_channel(944886185136894002)
    await channel.send(embed=MC.simpleMessage('Hey im online!'))

