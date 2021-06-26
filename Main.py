from Get_Image_Url import *
from discord import Client, Embed, Colour, Game
from time import time


client = Client()
token = "NzEwNDg0NTQzOTM2NjU5NTU4.Xr1ISw.BI551o4pyDeKJYalIZLnBjwBOm4"#"NzExNjEzMTQwMjk0NTY2MDE4.XsFjYQ.p5RrXCQgLTZ7UgYcfsnYBOh-Aog"

interactions_commands = ['!pat', '!kiss', '!hug', '!slap']
interactions_modeles = ['fez cafuné em', 'beijou', 'abraçou', 'deu um tapa em']


@client.event
async def on_ready():
    await client.change_presence(activity=Game('!help'))
    print('bot is on')


@client.event
async def on_message(message):
    if message.content == '!help':
        style = Embed(title='Help Message',
                description="""!img => for a random anime image\n
                               !img (argument) => to search an anime image\n
                               !wp => for a random anime wallpaper\n
                               !wp (argument) => to search an anime wallpaper\n
                               !gif => send a random anime gif\n
                               !gif (argument) => to search an anime gif\n
                               !slap (user) => slap the user\n
                               !hug (user) => hug the user\n
                               !kiss (user) => kiss the user\n
                               !pat (user) => pat the user""",
                color=Colour.random())
        await message.channel.send(embed=style)


    if message.content.startswith('!img'):
        s = time()
        search = message.content[len('!img'):]
        style = Embed(title='Image Request', color=Colour.random())
        image_url = get_image_url(f'https://safebooru.org//index.php?page=dapi&tags={search}&s=post&q=index', )
        style.set_image(url=image_url)
        f = time()
        print(f-s)
        await message.channel.send(embed=style)
        f = time()
        print(f-s)


    if message.content.startswith('!wp'):
        search = message.content[len('!wp'):]
        style = Embed(title='Wallpaper Request', color=Colour.random())
        image_url = get_image_url(f"https://safebooru.org/index.php?page=dapi&s=post&tags=wallpaper {search}&q=index")
        style.set_image(url=image_url)
        await message.channel.send(embed=style)


    if message.content.startswith('!gif'):
        search = message.content[len('!gif'):]
        style = Embed(title='Gif Request', color=Colour.random())
        image_url = get_gif_url(search)
        style.set_image(url=image_url)
        await message.channel.send(embed=style)


    for i in interactions_commands:
        if i in message.content.lower():
            image_url = get_gif_url(term=i.replace('!', ''))
            msg = f'<@{str(message.author.id)}> {interactions_modeles[interactions_commands.index(i)]} <@{message.mentions[0].id}>'
            style = Embed(description=msg, color=Colour.random())
            style.set_image(url=image_url)
            await message.channel.send(embed=style)
            break

client.run(token)
