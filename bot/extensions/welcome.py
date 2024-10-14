import hikari
import miru
import arc


plugin = arc.GatewayPlugin("Welcome")


@plugin.include
@arc.slash_command("ping", "Really?")
async def ping(ctx: arc.GatewayContext):
    await ctx.respond("pong")



@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
