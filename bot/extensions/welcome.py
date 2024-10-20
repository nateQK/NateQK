import hikari
import miru
import arc

from ..utils import configDB

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Welcome")

@plugin.include
@arc.slash_command("ping", "Really?")
async def ping(ctx: arc.GatewayContext):
    await ctx.respond("pong")

@plugin.include
@arc.slash_command("environment", "Tests the environment to see if you can access them")
async def environtest(ctx: arc.GatewayContext):
    await ctx.respond("cool!", flags=hikari.MessageFlag.EPHEMERAL)
    print(configDB.getHost)

@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
