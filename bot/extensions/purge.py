import hikari
import arc
import miru

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Purge")



@plugin.include
@arc.with_hook(arc.user_limiter(60, 1))
@arc.slash_command("purge", "Purges a select amount of messages")
async def purge(
    ctx: arc.GatewayContext,
    purge_length: arc.Option[int, arc.IntParams(description="How many messages to Delete?", min=1, max=100)]
) -> None:
    
    purgeEmbed: hikari.Embed = hikari.Embed(title="Deleted Messages", color='#f23914')
    
    purgeEmbed.add_field(name=f"Deleted messages", value=str(purge_length), inline=True)
    
    await ctx.respond(embed=purgeEmbed, flags=hikari.MessageFlag.EPHEMERAL)


@arc.loader
def load(client: arc.GatewayClient) -> None:
    client.add_plugin(plugin)

@arc.unloader
def unload(client: arc.GatewayClient) -> None:
    client.remove_plugin(plugin)
