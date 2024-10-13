import hikari
import arc
import miru
from os import path



bot = hikari.GatewayBot(token="", banner=None, intents=hikari.Intents.ALL)
client=arc.GatewayClient(bot)

client.load_extensions_from(path.join("bot", "extensions"))






