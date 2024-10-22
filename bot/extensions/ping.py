import hikari
import miru
import arc

from ..bot import BOT
from ..utils.database import Database

from ..utils import configDB

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Ping")

@plugin.include
@arc.slash_command("ping", "Get's bot Latency to discord Servers")
async def ping(ctx: arc.GatewayContext) -> None:
    """Responds to user calling command with bot latency to discord"""
    await ctx.respond(f"Ping! Bot Latency is {str(BOT.heartbeat_latency*100)[:-10]} Ms")


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
