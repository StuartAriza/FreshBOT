import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('OTc1MTAxMzU3Mjc3MTkyMjUy.GYmnKY.UZdzACohXFN_WSt2ijTZTLRfiCnwq9CguLKklU')