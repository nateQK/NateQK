'''Base bot containing things such as

BOT,
client,
and some listen events for starting the bot
'''
import hikari
import arc
import miru
from os import path
from loguru import logger

from .utils import configBOT, configDB, configVERSION



BOT: hikari.GatewayBot = hikari.GatewayBot(
    token=configBOT.getToken(),
    banner=None, 
    intents=hikari.Intents.ALL
)

client: arc.GatewayClient = arc.GatewayClient(BOT)
miruClient: miru.Client = miru.Client.from_arc(client)


client.load_extensions_from(path.join("bot", "extensions"))

@client.listen()
async def on_startup(event: arc.StartedEvent) -> None:
    print("[=] STARTED")
    logger.info(f"Bot Version: {configVERSION.getVersion()}")
