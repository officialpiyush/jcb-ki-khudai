import discord
import json
from discord.ext import commands

with open("./config.json") as f:
    config = json.load(f)

client = commands.Bot(
    command_prefix=config["prefix"],
    description="Reacts With a JCB Emoji to the message",
)


@client.event
async def on_ready():
    print(
        "     _  _____ ____  "
        "\n| |/ ____|  _ \ "
        "\n| | |    | |_) |"
        "\n| | |    |  _ < "
        "\n| |__| | |____| |_) |"
        "\n \____/ \_____|____/ "
    )
    print(f"Successfully logged in and booted...!")


@client.event()
async def on_message(msg: discord.Message):
    if msg.channel.id != config["channel"]:
        return
    else:
        emoji: discord.Emoji = await msg.guild.fetch_emoji(int(config["emote"]))
        await msg.add_reaction(emoji=emoji)
        return


client.run(config["token"])
