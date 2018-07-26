import re
import scrape
import discord
from builtins import str
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
familiardic = None
fusiondic = None
mythicdic = None

@bot.event
async def on_ready():
    global enlist
    global jplist
    global bothlist
    
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    enlist, jplist, bothlist = scrape.scrapeall()
    print('Ready')

@bot.command()
async def en(ctx, index=None):
    global enlist
    if index:
        index = int(index)
        enevent = enlist[index]
        embed = discord.Embed(title=enevent['bannerdict']['name'], description=enevent['bannerdict']['time'], color=0x7289da)
        embed.set_image(url=enevent['bannerdict']['img'])
        servantvalue = "".join(servant['rarity']+' '+servant['name']+'\n' for servant in enevent['servantlist'])
        embed.add_field(name='Servants', value=(servantvalue if servantvalue else "None"), inline=False)
        craftessencevalue = "".join(craftessence['rarity']+' '+craftessence['name']+'\n' for craftessence in enevent['craftessencelist'])
        embed.add_field(name='Craft Essences', value=(craftessencevalue if craftessencevalue else "None"), inline=False)
    else:
        embed = discord.Embed(title='EN Events', color=0x7289da)
        for i, enevent in enumerate(enlist):
            embed.add_field(name=str(i)+'. '+enevent['bannerdict']['name'], value=enevent['bannerdict']['time'], inline=False)
    await ctx.send(embed=embed)
    
@bot.command()
async def jp(ctx, index=None):
    global jplist
    if index:
        index = int(index)
        jpevent = jplist[index]
        embed = discord.Embed(title=jpevent['bannerdict']['name'], description=jpevent['bannerdict']['time'], color=0x7289da)
        embed.set_image(url=jpevent['bannerdict']['img'])
        servantvalue = "".join(servant['rarity']+' '+servant['name']+'\n' for servant in jpevent['servantlist'])
        embed.add_field(name='Servants', value=(servantvalue if servantvalue else "None"), inline=False)
        craftessencevalue = "".join(craftessence['rarity']+' '+craftessence['name']+'\n' for craftessence in jpevent['craftessencelist'])
        embed.add_field(name='Craft Essences', value=(craftessencevalue if craftessencevalue else "None"), inline=False)
    else:
        embed = discord.Embed(title='EN Events', color=0x7289da)
        for i, jpevent in enumerate(jplist):
            embed.add_field(name=str(i)+'. '+jpevent['bannerdict']['name'], value=jpevent['bannerdict']['time'], inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="FGOCirnopediaBot", description="All information from http://fate-go.cirnopedia.org", color=0x7289da)
    
    # give info about you here
    embed.add_field(name="Author", value="ranthai")

    # give users a link to invite thsi bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="FGOCirnopediaBot", description="List of commands are:", color=0x7289da	)
    embad.add_field(name="$update", value="Update to current cirnopedia event info", inline=False)
    embed.add_field(name="$en", value="Gives EN event info", inline=False)
    embed.add_field(name="$jp", value="Gives JP event info", inline=False)
    embed.add_field(name="$both", value="Gives both event info.", inline=False)
    embad.add_field(name="$info", value="Gives this bot's info", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    
    await ctx.send(embed=embed)
    
bot.run('')