import discord

TOKEN = 'Njk5MTgyNzI5Mzg4MDk3NTc4.XpQqtQ.ThnCS3Zlg0XXX-dp0z1iBedtt6o'

client = discord.Client()

@client.event
async def on_message(message):
    await message.channel.send("YOU SUC")

client.run(TOKEN)
