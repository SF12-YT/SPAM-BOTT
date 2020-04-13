import discord

TOKEN = 'NjkxOTg3OTUwNDA1MTU2ODg3.Xnw4yw.g9zF6eFOu-B0BfS45RGtBNw3_Os'

client = discord.Client()

@client.event
async def on_message(message):
    while True:
        await message.channel.send("YOU SUC")

client.run(TOKEN)