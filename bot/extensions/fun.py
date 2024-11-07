import hikari
import arc
from ..bot import BOT
#import miru
from loguru import logger
import requests
from json import loads
from typing import Any
from random import choice
from pydantic import BaseModel

plugin: arc.GatewayPlugin = arc.GatewayPlugin("Fun")
version: str = "1.0"

# NOTE: https://api.dictionaryapi.dev/api/v2/entries/en/
# Funny Dictionary api


@plugin.include
@arc.slash_command("fun-version", "Get's current version of fun Extensions")
async def funVersion(ctx: arc.GatewayContext):
  await ctx.respond(version, flags=hikari.MessageFlag.EPHEMERAL)


#@plugin.include
#@arc.slash_command("dictionary","Checks your word against a publicily available Dictionary, %100 unaltered")
async def dictionary(
  ctx: arc.GatewayContext,
  word: arc.Option[str, arc.StrParams()]
) -> None:
  word = word.lower()

  req: requests.Response = requests.get(f"{word}")

  await ctx.respond(req.json())



@plugin.include
@arc.with_hook(arc.user_limiter(60, 5))
@arc.slash_command('dog', "Show's an image of a cute dog")
async def dog_fetch(ctx: arc.GatewayContext):
  req: requests.Response = requests.get("https://dog.ceo/api/breeds/image/random")
  reqData: Any = req.json()

  await ctx.respond(reqData["message"])




@plugin.include
@arc.with_hook(arc.user_limiter(60, 5))
@arc.slash_command('cat', "Show's an image of a cute dog")
async def cat_fetch(ctx: arc.GatewayContext):
  headers = {'accept': 'image/*'}
  req: requests.Response = requests.get("https://cataas.com/cat?json=true", headers=headers)
  reqData: Any = req.json()
  await ctx.respond(f"https://cataas.com/cat/{reqData["_id"]}")



@plugin.include
@arc.with_hook(arc.user_limiter(60, 60))
@arc.with_hook(arc.guild_only)
@arc.slash_command("source", "I'm a fact checker, Here's my source!!!")
async def source(
  ctx: arc.GatewayContext,
  question: arc.Option[str, arc.StrParams()]
):
  if ctx.guild_id != None:
    members: int = await BOT.rest.fetch_members(ctx.guild_id).count()
  else: members = 0

  answers: list[str] = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don’t count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    "Try killing yourself",
    "Why tf would you ask me?",
    "Maybe",
    "Bruh, ask again",
    "Ask Trump bro",
    "Trump says no bro",
    "Trump says yes bro",
    "Ask Kamala bro",
    "Kamala says yes bro",
    "Kamala says no bro",
    "Not A Trump Supporter? Try Asking Kamala",
    "Not A Kamala Supporter? Try Asking Trump",
    "Kamala Failed, hmm. don't try biden",
    "This command gonna get me cancelled. but no to your question",
    "This was written by a monkey, wasn't it...",
    f"You know, I see {members-1} Others that can answer that question",
    "NOOOOOO. Don't make me @ㅤeveryone",
  ]
  ballembed: hikari.Embed = hikari.Embed(title="My Sources say...")
  mychoice: Any = choice(answers)
  ballembed.add_field("Question", question, inline=False)
  ballembed.add_field("Answer", mychoice, inline=False)

  await ctx.respond(embed=ballembed)


@plugin.include
@arc.slash_command("dad", "Tells you a REAAALLLLY funny joke")
async def dad_joke(ctx: arc.GatewayContext):
  req: requests.Response = requests.get("")
  req.json()


@plugin.include
@arc.slash_command("useless", "Gives you an Utterly useless fact to use in, no way shape or form later")
async def useless_fact(ctx: arc.GatewayContext) -> None:
  req: requests.Response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
  reqData: Any = req.json()

  await ctx.respond(reqData["text"])





@plugin.set_error_handler
async def error_handler(ctx: arc.GatewayContext, exc: Exception) -> None:
    logger.debug(type(exc))
    logger.debug(exc)
    if isinstance(exc, arc.errors.UnderCooldownError):
        await ctx.respond(exc, flags=hikari.MessageFlag.EPHEMERAL)
        return


@arc.loader
def load(Client: arc.GatewayClient) -> None:
  logger.info(f"Loading {plugin.name} Plugin")
  Client.add_plugin(plugin)

@arc.unloader
def unload(Client: arc.GatewayClient) -> None:
  logger.info(f"Un-Loading {plugin.name} Plugin")
  Client.remove_plugin(plugin)
