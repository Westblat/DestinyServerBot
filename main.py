import discord
from discord.ext import commands
from credentials import destiny, chat_id

shit = discord.Client()
client = commands.Bot(command_prefix="!")
message = None
emojis = [discord.PartialEmoji(name="🐒"), discord.PartialEmoji(name="👑"), discord.PartialEmoji(name="🧙")]
emojis_and_ranks = {"🐒": "Hunter", "👑": "Titan", "🧙": "Warlock"}


# 532844472400 Permissions 534992387184  https://discord.com/oauth2/authorize?client_id=993212430509424649&scope=bot&permissions=534992387184
@client.event
async def on_ready():
    # 351285503116443668
    channel = await client.fetch_channel(chat_id)
    new_message = await channel.send("Emote here to get role")
    global message
    message = new_message
    global emojis
    for emoji in emojis:
        await message.add_reaction(emoji)
    print("The bot is online")


@client.event
async def on_raw_reaction_add(context):
    global message
    global emojis_and_ranks
    user = context.member
    if context.message_id == message.id and not user.bot:
        name = emojis_and_ranks[context.emoji.name]
        role = discord.utils.get(user.guild.roles, name=name)
        if role in user.roles:
            await user.remove_roles(role)
        else:
            await user.add_roles(role)
        await message.remove_reaction(context.emoji, user)


# client.run("") Joukkue
client.run(destiny)
