import hikari
import hikari-arc
import hikari-miru

from environment import *

BOT = hikari.GatewayBot(token=TOKEN, banner=None, intents=hikari.Intents.ALL)
