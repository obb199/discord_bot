"""
To save and load configs of bot.
"""


def open_configs(*args):  # args = sets with channels ID
    try:
        # Opening datas
        with open('SERVER_CONFIG.txt', 'r') as configs:
            # Values to delete from any line of datas
            names = ('MEMES', 'POLNEWS', 'GLOBNEWS', 'DAILYNEWS', 'TECHNEWS', 'ECONOMYNEWS', 'COINS', 'DIGCOINS')
            user_configs = configs.readlines()

            for index in range(len(args)):
                if user_configs[index].split(':')[1] != 'None\n':  # If line has some channel ID
                    configs = user_configs[index].split(':')

                    for channels in configs:
                        if channels != names[index] and channels != '\n':
                            args[index].add(int(channels))

    except FileNotFoundError:
        return "Save doesn't exist"


def saving_configs(memes, pol, glob, daily, tech, economy, coins, digcoins):  # Sets with channels ID
    with open('SERVER_CONFIG.txt', 'w') as save:
        if len(memes) == 0:   # No channels
            save.write(f'MEMES:None\n')
        else:  # Some channels on the set
            save.write(f'MEMES:')
            for channels in memes:
                save.write(f'{channels}:')
            save.write('\n')

        if len(pol) == 0:
            save.write(f'POLNEWS:None\n')
        else:
            save.write(f'POLNEWS:')
            for channels in pol:
                save.write(f'{channels}:')
            save.write('\n')

        if len(glob) == 0:
            save.write(f'GLOBNEWS:None\n')
        else:
            save.write(f'GLOBNEWS:')
            for channels in glob:
                save.write(f'{channels}:')
            save.write('\n')

        if len(daily) == 0:
            save.write(f'DAILYNEWS:None\n')
        else:
            save.write(f'DAILYNEWS:')
            for channels in daily:
                save.write(f'{channels}:')
            save.write('\n')

        if len(tech) == 0:
            save.write(f'TECHNEWS:None\n')
        else:
            save.write(f'TECHNEWS:')
            for channels in tech:
                save.write(f'{channels}:')
            save.write('\n')

        if len(economy) == 0:
            save.write(f'ECONOMYNEWS:None\n')
        else:
            save.write(f'ECONOMYNEWS:')
            for channels in economy:
                save.write(f'{channels}:')
            save.write('\n')

        if len(coins) == 0:
            save.write(f'COINS:None\n')
        else:
            save.write(f'COINS:')
            for channels in coins:
                save.write(f'{channels}:')
            save.write('\n')

        if len(digcoins) == 0:
            save.write(f'DIGCOINS:None\n')
        else:
            save.write(f'DIGCOINS:')
            for channels in digcoins:
                save.write(f'{channels}:')
            save.write('\n')
