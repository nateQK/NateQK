'''A set of commands that are not allowed to be disabled'''
# NOTE: This plugin doesn't get an unloader function, this one should always be on

import hikari
import miru
import arc

from ..bot import client, BOT
from ..utils import configVERSION

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Immutable")
version: str = "1.0"

activityTypes: dict = {
    'Watching': hikari.ActivityType.WATCHING,
    'Listening': hikari.ActivityType.LISTENING,
    'Streaming': hikari.ActivityType.STREAMING,
    'Playing': hikari.ActivityType.PLAYING
}

statusTypes: dict = {
  'Online': hikari.Status.ONLINE,
  'Do Not Disturb': hikari.Status.DO_NOT_DISTURB,
  'Idle': hikari.Status.IDLE,
}



# NOTE: set bot presence
@client.listen()
async def set_presence(event: arc.StartedEvent):
  await BOT.update_presence(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(name=f'A Game Engine Community', type=hikari.ActivityType.WATCHING)
    )


@plugin.include
@arc.slash_command("version", "Prints information about the current version of the bot and if an update is available")
async def versions(ctx: arc.GatewayContext) -> None:
  # INFO: This is not ready yet, but the code should work preetty simply
  versionEmbed: hikari.Embed = hikari.Embed(title='Version', url="https://nateqk.github.io/")
  current:str = configVERSION.getVersion()
  latest:str = configVERSION.latestVersion()

  versionEmbed.add_field(name="Current Version", value=current)
  if current != latest:
    versionEmbed.colour = hikari.Color(int("ff0000"))
    versionEmbed.add_field(name="Latest Version", value=latest)
    if current[0] != latest[0]:
      versionEmbed.add_field(name="Update Recommended", value="You're at least 1 major version behind! Check Upgrade notes to ensure you upgrade properly")
      versionEmbed.url = f"https://nateqk.github.io/upgrade/{current[0]}/to/{latest[0]}"

    await ctx.respond(embed=versionEmbed)




@arc.loader
def loader(Client: arc.GatewayClient):
    Client.add_plugin(plugin)

