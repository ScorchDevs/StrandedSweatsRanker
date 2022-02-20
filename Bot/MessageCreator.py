import discord

class MessageCreator():
    name = 'SSG'
    version = '1.0'
    
    def simpleMessage(self, message):
        embed = discord.Embed(colour=discord.Colour.green(), description = message)
        embed.set_footer(text=f"{self.name}v{self.version} by Council", icon_url='https://cdn.discordapp.com/app-icons/944877395696058388/4c2e17d3c85db9a9ff588191508afab5.png')
        return embed
        