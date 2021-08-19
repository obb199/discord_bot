"""
Here you find other web scrapping, to find links of memes. All links used stay on a txt archive to bot don't send
the same link.
"""
from urllib.request import urlopen
from time import sleep


def memes_search():
    link = "https://imgur.com/search/time?q=memes&qs=thumbs"

    html_code = urlopen(link).read().decode("utf-8")
    html_code = html_code.split(' ')

    with open('used_memelinks.txt', 'r') as links:
        used_links = links.readlines()

    for count in range(len(used_links)):
        used_links[count] = used_links[count][0:-1]

    new_link = None
    for links in html_code:
        if '/gallery/' in links and 'Factory' not in links and "https://imgur.com" + links[6:-1] not in used_links:
            new_link = "https://imgur.com" + links[6:-1]

            with open('used_memelinks.txt', 'a') as arq:
                arq.write(new_link)
                arq.write('\n')

        if new_link is not None:
            sleep(5)
            return new_link

    sleep(5)

    return 'no memes here'
