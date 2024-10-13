import hikari
import arc
import miru

from environment import *

BOT = hikari.GatewayBot(token=TOKEN, banner=None, intents=hikari.Intents.ALL)
