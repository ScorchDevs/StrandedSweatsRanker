import discord
from MessageCreator import MessageCreator
bot = discord.Client()
MC = MessageCreator()


def start_bot(token: str):
    bot.run(token)
