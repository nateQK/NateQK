import hikari
import arc
from loguru import logger
from datetime import datetime
from ..utils import configBOT
import requests
from pydantic import BaseModel as base
from pydantic import Field
#from apscheduler.schedulers.asyncio import AsyncIOScheduler
from typing import Any


class reactionsDict(base):
  url: str
  total_count: int
  plus1: Any = Field(alias="+1", description="idk man") # type: ignore
  minus1: Any = Field(alias="-1", description="idk man") # type: ignore
  laugh: int
  hooray: int
  confused: int
  heart: int
  rocket: int
  eyes: int

class prDict(base):
  url: str
  html_url: str
  diff_url: str
  patch_url: str
  merged_at: str | None


class userDict(base):
  login: str
  id: int
  node_id: str
  avatar_url: str
  gravatar_id: str
  url: str
  html_url: str
  followers_url: str
  following_url: str
  gists_url: str
  starred_url: str
  subscriptions_url: str
  organizations_url: str
  repos_url: str
  events_url: str
  received_events_url: str
  userType: str | None = None
  user_view_type: str
  site_admin: bool


class internalIssues(base):
  url: str
  repository_url: str
  labels_url: str
  comments_url: str
  events_url: str
  html_url: str
  id: int
  none_id: str | None = None
  number: int
  title: str
  user: userDict
  labels: list[str]
  state: str
  locked: bool
  assignee: str | None
  assignees: list[str]
  milestone: str | None
  comments: int
  created_at: str 
  updated_at: str
  closed_at: str | None
  author_association: str
  active_lock_reason: str | None
  draft: bool
  pull_request: prDict
  body: str
  closed_by: str | None
  reactions: reactionsDict
  timeline_url: str
  performed_via_github_app: str | None
  state_reason: str | None = None






plugin: arc.GatewayPlugin = arc.GatewayPlugin("Useful")

#scheduler: AsyncIOScheduler = AsyncIOScheduler()
timeChoices: list[str]  = ["m", "h", "d"]
# TODO: This should be moved to something configurable using {org-name} and {repo-name}
issuesUrl: str = "https://api.github.com/repos/blazium-engine/blazium/issues"

async def steal_time(time:str) -> datetime:
  print(time)


  return datetime.now()



@plugin.include
@arc.slash_command("issues", "Cycle Through Github issues in the github")
async def issues(ctx: arc.GatewayContext) -> None:
  headers: dict[str, str] = {
    "accept": "application/vnd.github.raw+json"
  }
  response = requests.get(issuesUrl, headers=headers)
  if response.status_code == 200:
    pass
  elif response.status_code == 422:
    await ctx.respond("Validation failed, or the endpoint has been spammed.")
    return
  else:
    await ctx.respond(f"An error has occured, We got a status code of {response.status_code} ping Naterfute and Bioblaze Payne")
    return

  issues: internalIssues = internalIssues(**response.json()[0])
  print(issues.id)
  #logger.error(issues)
  




@plugin.include
@arc.slash_command("links","Responds with a link to all the stores blazium is on!")
async def links(ctx: arc.GatewayContext) -> None:
  em: hikari.Embed = hikari.Embed(title="Blazium Store Pages")
  # TODO: Replace hardcoded links with links put into the database through a command
  # It should be done in such a way that it's not inconveinent or slow,
  # the command should do the following
  # - Start a modal using hikari-miru
  # Ask the following questions
  # - Title
  # - Description

  em.set_author(name="NaterBot", icon=str(configBOT.getBotPFP()))
  em.add_field("Github", "https://github.com/blazium-engine/blazium/releases")
  em.add_field("Itch.io", "https://blaziumengine.itch.io/")
  em.add_field("Steam", "https://store.steampowered.com/app/3293450/Blazium_Engine/)")
  em.set_footer("Blazium Community Bot", icon=str(configBOT.getBotPFP()))
  await ctx.respond(embed=em)



#@plugin.include
#@arc.slash_command("remind", "Pings you in a set amount of hours")
#async def remind(
#  ctx: arc.GatewayContext,
#  time: arc.Option[str, arc.StrParams()],
#  units: arc.Option[str, arc.StrParams(choices=timeChoices)]
#):
#  pass


@arc.loader
def load(client: arc.GatewayClient) -> None:
    logger.info(f"Loading {plugin.name} Plugin")
    client.add_plugin(plugin)

@arc.unloader
def unloader(client: arc.GatewayClient) -> None:
    logger.info(f"Un-Loading {plugin.name} Plugin")
    client.remove_plugin(plugin)
