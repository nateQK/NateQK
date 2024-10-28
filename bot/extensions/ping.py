import hikari
import miru
import arc

from ..bot import BOT
from ..utils.database import Database

from ..utils import configDB

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Ping")
version: str = "1.0"



@plugin.include
@arc.slash_command("ping", "Get's bot Latency to discord Servers")
async def ping(ctx: arc.GatewayContext, /) -> None:
    """Responds to user calling command with bot latency to discord"""
    botPing: float= float(str(BOT.heartbeat_latency*100)[:-10])
    pingEmbed: hikari.Embed = hikari.Embed()
    
    pingEmbed.title = "Ping!"
    if botPing < 35: pingEmbed.color = hikari.Color(int("15cdf2"))
    elif botPing < 50: pingEmbed.color = hikari.Color(int("d2f884"))
    elif botPing > 50: pingEmbed.color = hikari.Color(int("c73ea2"))
    elif botPing > 200: pingEmbed.color = hikari.Color(int("ff0000"))

    if botPing > 200:
        pingEmbed.add_field(name="Latency!??!?!?!", value=f'{botPing} Ms', inline=True)
        pingEmbed.add_field(name="WHY!!!!", value="Is your server running in a chinese basement???")
    else:
        pingEmbed.add_field(name="Latency", value=f'{botPing} Ms')
    
    await ctx.respond(embed=pingEmbed)


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
