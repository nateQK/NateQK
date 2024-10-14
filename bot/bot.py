import hikari
import arc
import miru
from os import path



bot = hikari.GatewayBot(token="", banner=None, intents=hikari.Intents.ALL)
client=arc.GatewayClient(bot)

client.load_extensions_from(path.join("bot", "extensions"))

# it's midnight wtf am I writing
# This code gets called write after the extensions get loaded
@client.listen()
async def on_startup(event: arc.StartedEvent):
    # Jesus Fucking Christ, you have got to be kidding me
    # This is not a 2012 minecraft video
    print("Blazing new trails")





