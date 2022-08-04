import discord
from discord.ext import commands
from credentials import destiny, chat_id, joukkue_chat_id, joukkue

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
    # Create new message and save it to the global variable
    new_message = await channel.send("Add one of the reactions to get yourself a main class role. If you want to get rid of one of the roles, just add the reaction again. \n🐒 = Hunter \n👑 Titan \n🧙Warlock")
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
        try:
            # Add correct role based on emoji when user reacts to the correct message
            name = emojis_and_ranks[context.emoji.name]
            role = discord.utils.get(user.guild.roles, name=name)
            if role in user.roles:
                # If there is role already, remove old
                await user.remove_roles(role)
            else:
                # If no role, add the role
                await user.add_roles(role)
            await message.remove_reaction(context.emoji, user)
        except KeyError:
            # If someone adds stupid emojis, remove them
            await message.remove_reaction(context.emoji, user)


@client.event
async def on_message(context):
    if context.channel.id == int(chat_id) and not context.author.bot:
        # Someone posts stupid shit, we delete it
        await context.delete()

# client.run("joukkue") Joukkue
client.run(destiny)
