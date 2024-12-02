'''Base bot containing things such as

BOT,
client,
and some listen events for starting the bot
'''
import hikari
import arc
import miru
from os import path
from sys import stderr
from loguru import logger
from typing import Any

from .utils import configBOT, configVERSION

def debug_init(trace: bool = False, debug: bool = False):
    logger.remove()
    if debug:
        logger.add(stderr, level='DEBUG')
    elif trace:
        logger.add(stderr, level='TRACE')
    else:
        logger.add(stderr, level='INFO')
        pass
    pass

debug_init(False, False)
logger.debug("Debug is Working")
logger.trace("Trace is Working")
logger.error("Error is Working")
logger.info("Info is Working")
logger.warning("Warning is Working")
logger.success("Success is Working")
logger.critical("Critical is Working")


BOT: hikari.GatewayBot = hikari.GatewayBot(
    token=configBOT.getToken(),
    banner=None,
    intents=hikari.Intents.ALL,
)

client: arc.GatewayClient = arc.GatewayClient(BOT)
miruClient: miru.Client = miru.Client.from_arc(client)


client.load_extensions_from(path.join("bot", "extensions"))

@client.listen()
async def on_startup(event: arc.StartedEvent[Any]) -> None:
    #print("[=] STARTED")
    logger.info(f"Bot Version: {configVERSION.getVersion()}")
