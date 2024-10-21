import hikari
import miru
import arc

from ..bot import BOT
from ..utils.database import Database

from ..utils import configDB

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Welcome")

@plugin.include
@arc.slash_command("ping", "Really?")
async def ping(ctx: arc.GatewayContext):
    """Returns with bot latency to server"""
    await ctx.respond(f"Ping! Bot Latency is {str(BOT.heartbeat_latency*100)[:-10]} Ms")

@plugin.include
@arc.slash_command("environment", "Tests the environment to see if you can access them")
async def environtest(ctx: arc.GatewayContext):
    await ctx.respond("cool!", flags=hikari.MessageFlag.EPHEMERAL)
    print(configDB.getHost)

@plugin.include
@arc.slash_command("dbtest", "Testing database")
async def dbtest(ctx: arc.GatewayContext):
    await ctx.respond(f"{Database.getClient}")


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
