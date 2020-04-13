import discord

TOKEN = 'Njk5MTgyNzI5Mzg4MDk3NTc4.XpQ1bA.pxdg1ixt7K4t2Ru-f_2ZNwH4Db0'

client = discord.Client()

@client.event
async def on_message(message):
    await message.channel.send("YOU SUC")

client.run(TOKEN)
