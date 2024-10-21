import hikari
import arc
import miru
from os import path

from .utils import configBOT, configDB

BOT: hikari.GatewayBot = hikari.GatewayBot(
    token=configBOT.getToken,
    banner=None, 
    intents=hikari.Intents.ALL
)

client: arc.GatewayClient = arc.GatewayClient(BOT)

client.load_extensions_from(path.join("bot", "extensions"))

@client.listen()
async def on_startup(event: arc.StartedEvent):
    print("[=] STARTED")
