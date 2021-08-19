import asyncio
import discord
import TOKEN_value
import news
import memes
import coins_value
import saveconfigs
from datetime import datetime

client = discord.Client()
TOKEN = TOKEN_value.token()

memes_channels = set()
pol_channels = set()
glob_channels = set()
daily_channels = set()
technology_channels = set()
economy_channels = set()
coins_channels = set()
digitalcoins_channels = set()

start = False
coins_used = False
digitalcoins_used = False


@client.event
async def on_ready():
    print('BOT HAS BEEN CONNECTED.')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    global start

    if message.content.lower().startswith("!help") or message.content.lower().startswith("!commands"):
        #  Embed é estilização
        description = discord.Embed(
            title="Commands of Waiter: ",
            color=discord.Color.gold(),
            description="- !GlobalNews - if you want to see the news from all our world\n\n"
                        "- !PoliticalNews - If you want to see the political news from Brazil\n\n"
                        "- !EconomyNews - If you want to see economy news\n\n"
                        "- !TechnologyNews - If you want to see technology news\n\n"
                        "- !DailyNews - If you want to see generalists news\n\n"
                        "- !CoinsPrice - If you want to receive prices of coins\n\n"
                        "- !DigitalCoinsPrice - If you want to receive prices of digital coins\n\n"
                        "- !Memes - If you want to smile\n\n"
                        "- !Removes - Too see commands to remove some utility\n\n"
                        "- !SaveConfigs - To save current settings\n\n"
                        "- !LoadConfigs - To load the last settings that you saved\n\n"
                        "- !Start - To run the utilities\n\n"
        )
        await message.channel.send(embed=description)

    if message.content.lower().startswith("!removes"):
        removes = discord.Embed(
            title="Commands To remove Something: ",
            description="- !RemoveGlobal - To remove Global News from currently channel\n\n"
                        "- !RemovePolitical - To remove Political News from currently channel\n\n"
                        "- !RemoveEconomy - To remove Economy News from currently channel\n\n"
                        "- !RemoveTechnology - To remove Technology News from currently channel\n\n"
                        "- !RemoveDaily - To remove Daily News from currently channel\n\n"
                        "- !RemoveCoins - To remove Coins Price from currently channel\n\n"
                        "- !RemoveDigitalCoins - To remove Digital Coins Price from currently channel\n\n"
                        "- !RemoveMemes - To remove Memes from currently channel\n\n"
        )
        await message.channel.send(embed=removes)

    if message.content.lower().startswith('!memes'):
        await message.channel.send("This channel is added to receive memes after bot was started")
        memes_channels.add(message.channel.id)

    if message.content.lower().startswith('!removememes'):
        await message.channel.send("This channel don't gonna receive more memes")
        memes_channels.discard(message.channel.id)

    if message.content.lower().startswith("!politicalnews"):
        await message.channel.send("This channel is added to receive political news after bot was started")
        pol_channels.add(message.channel.id)

    if message.content.lower().startswith("!removepolitical"):
        await message.channel.send("This channel don't gonna receive more Political News")
        pol_channels.discard(message.channel.id)

    if message.content.lower().startswith("!globalnews"):
        await message.channel.send("This channel is added to receive global news after bot was started")
        glob_channels.add(message.channel.id)

    if message.content.lower().startswith("!removeglobal"):
        await message.channel.send("This channel don't gonna receive more Global News")
        glob_channels.discard(message.channel.id)

    if message.content.lower().startswith("!dailynews"):
        await message.channel.send("This channel is added to receive daily news after bot was started")
        daily_channels.add(message.channel.id)

    if message.content.lower().startswith("!removedaily"):
        await message.channel.send("This channel don't gonna receive more Daily News")
        daily_channels.discard(message.channel.id)

    if message.content.lower().startswith("!technologynews"):
        await message.channel.send("This channel is added to receive technology news after bot was started")
        technology_channels.add(message.channel.id)

    if message.content.lower().startswith("!removetechnology"):
        await message.channel.send("This channel don't gonna receive more Technology News")
        technology_channels.discard(message.channel.id)

    if message.content.lower().startswith("!economynews"):
        await message.channel.send("This channel is added to receive economy news after bot was started")
        economy_channels.add(message.channel.id)

    if message.content.lower().startswith("!removeeconomy"):
        await message.channel.send("This channel don't gonna receive more Economy News")
        economy_channels.discard(message.channel.id)

    if message.content.lower().startswith('!coinsprice'):
        await message.channel.send("This channel is added to receive the values of some coins "
                                   "converted in Braziliam Real")
        coins_channels.add(message.channel.id)

    if message.content.lower().startswith('!removecoins'):
        await message.channel.send("This channel don't gonna receive more converted coins values")
        coins_channels.discard(message.channel.id)

    if message.content.lower().startswith('!digitalcoinsprice'):
        await message.channel.send("This channel is added to receive the values of some digital coins "
                                   "converted in Braziliam Real")
        digitalcoins_channels.add(message.channel.id)

    if message.content.lower().startswith('!removedigitalcoins'):
        await message.channel.send("This channel don't gonna receive more converted digital coins values")
        digitalcoins_channels.discard(message.channel.id)

    if message.content.lower().startswith('!saveconfigs'):
        await save_configs()
        await message.channel.send('Your configurations has been saved!')

    if message.content.lower().startswith('!loadconfigs'):
        await load_configs()
        await message.channel.send('Your configurations has been loaded!')

    if message.content.lower().startswith('!start'):
        start = True
        await message.channel.send("Utilities will run now!")

    while start:
        if len(coins_channels) > 0:
            await coins_price()

        if len(digitalcoins_channels) > 0:
            await digitalcoins_price()

        if len(memes_channels) > 0:
            await memes_loop()

        if len(pol_channels) > 0:
            await news_loop('political')

        if len(glob_channels) > 0:
            await news_loop('global')

        if len(daily_channels) > 0:
            await news_loop('daily')

        if len(economy_channels) > 0:
            await news_loop('economy')

        if len(technology_channels) > 0:
            await news_loop('technology')


async def memes_loop():
    meme = memes.memes_search()

    if meme != 'no memes here' and meme is not None:
        for channel_id in memes_channels:
            channel = client.get_channel(channel_id)
            await channel.send(meme)


async def news_loop(seed):
    news_link = news.news_search(seed)

    if news_link != 'no news':
        if seed == 'political':
            for channel_id in pol_channels:
                channel = client.get_channel(channel_id)
                await channel.send(news_link)

        if seed == 'global':
            for channel_id in glob_channels:
                channel = client.get_channel(channel_id)
                await channel.send(news_link)

        if seed == 'daily':
            for channel_id in daily_channels:
                channel = client.get_channel(channel_id)
                await channel.send(news_link)

        if seed == 'economy':
            for channel_id in economy_channels:
                channel = client.get_channel(channel_id)
                await channel.send(news_link)

        if seed == 'technology':
            for channel_id in technology_channels:
                channel = client.get_channel(channel_id)
                await channel.send(news_link)


async def coins_price():
    global coins_used

    time = datetime.now()
    hours = str(time)[11:13]
    minutes = str(time)[14:16]

    if (hours == '13' and minutes == '15' and not coins_used) or \
            (hours == '18' and minutes == '15' and not coins_used) or \
            (hours == '22' and minutes == '15' and not coins_used):

        prices = coins_value.coins_value()
        coins_used = True

        for channel_id in coins_channels:
            channel = client.get_channel(channel_id)
            prices_message = discord.Embed(title='Prices comparisons with Braziliam Real',
                                           colour=discord.colour.Colour.gold(),
                                           description=prices)
            await channel.send(embed=prices_message)

    if (hours == '13' and minutes == '20' and coins_used) or \
            (hours == '18' and minutes == '20' and coins_used) or \
            (hours == '23' and minutes == '20' and coins_used):
        coins_used = False


async def digitalcoins_price():
    global digitalcoins_used
    time = datetime.now()
    hours = str(time)[11:13]
    minutes = str(time)[14:16]

    if (hours == '13' and minutes == '30' and not digitalcoins_used) or \
            (hours == '18' and minutes == '30' and not digitalcoins_used) or \
            (hours == '22' and minutes == '30' and not digitalcoins_used):

        prices = coins_value.digital_coins_value()
        digitalcoins_used = True

        for channel_id in digitalcoins_channels:
            channel = client.get_channel(channel_id)
            prices_message = discord.Embed(title='Prices comparisons with Braziliam Real',
                                           colour=discord.colour.Colour.dark_gold(),
                                           description=prices)
            await channel.send(embed=prices_message)

    if (hours == '13' and minutes == '35' and digitalcoins_used) or \
            (hours == '18' and minutes == '35' and digitalcoins_used) or \
            (hours == '23' and minutes == '35' and digitalcoins_used):
        digitalcoins_used = False


async def save_configs():
    saveconfigs.saving_configs(memes_channels, pol_channels, glob_channels, daily_channels, technology_channels,
                               economy_channels, coins_channels, digitalcoins_channels)


async def load_configs():
    saveconfigs.open_configs(memes_channels, pol_channels, glob_channels, daily_channels, technology_channels,
                             economy_channels, coins_channels, digitalcoins_channels)


asyncio.gather(client.run(TOKEN), digitalcoins_price(), memes_loop(), news_loop(), coins_price(), save_configs(),
               load_configs())
