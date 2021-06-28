from randomcolor import RandomColor
from colormap import hex2rgb
from discord import Client, Game, Color, Embed

token = "NzEwNDg0NTQzOTM2NjU5NTU4.Xr1ISw.BI551o4pyDeKJYalIZLnBjwBOm4" #"ODU5MTQ3ODAxNjE0MzUyMzk0.YNodvg.JF6teJurHo5WorOGe60o8LjXYhA"

client = Client()
emoji = "❤️"


@client.event
async def on_ready():
    await client.change_presence(activity=Game('$help'))
    print('bot is on')


@client.event
async def on_reaction_add(reaction, user):
    role_id = None
    message = reaction.message
    if message.author.bot and "#" in message.content:
        color = message.content[message.content.find("#"):]
        rgb = hex2rgb(color)
        guild = client.guilds[0]
        roles_name, roles_id = [role.name for role in guild.roles], [role.id for role in guild.roles]
        user_roles, user_roles_name = [role for role in user.roles], [role.name for role in user.roles]

        if color not in roles_name:
            role_id = await guild.create_role(name=color, colour=Color.from_rgb(rgb[0], rgb[1], rgb[2]))
        else:
            for i in range(len(roles_name)):
                if i == color:
                    role_id = roles_id[i]
                    break

        for i in range(len(user_roles_name)):
            if "#" in user_roles_name[i]:
                await user.remove_roles(user_roles[i])
        if not user.bot:
            await user.add_roles(role_id)


@client.event
async def on_message(message):
    if not message.author.bot:
        if "$help" in message.content.lower():
            style = Embed(title='$help command', description='''$get (hex of the color)=> get a specific color\n
                                        $color =>generate a random color ''', color=Color.random())
            await message.channel.send(embed=style)

        if "$get" in message.content.lower():
            color = message.content.replace("$get ", "")
            try:
                rgb = hex2rgb(color)
                style = Embed(title=f'hex color: {color}',
                              color=Color.from_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2])))
                bot_msg = await message.channel.send(f"<@{str(message.author.id)}> {color}", embed=style)
            except ValueError:
                style = Embed(title='Error usage', description='use $get (hex color)',
                              color=Color.random())
                bot_msg = await message.channel.send(embed=style)
            await bot_msg.add_reaction(emoji)

        if "$color" in message.content.lower():
            color = RandomColor().generate()
            rgb = hex2rgb(color[0])
            style = Embed(title=f'color = hex color: {color[0]}',
                          color=Color.from_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2])))
            bot_msg = await message.channel.send(f"<@{str(message.author.id)}> {color[0]}", embed=style)
            await bot_msg.add_reaction(emoji)


client.run(token)
