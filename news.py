"""
Here you find other web scrapping, to find links of news. All links used stay on a txt archive to bot don't send
the same link twice.
"""

from urllib.request import urlopen


def news_search(seed):

    if seed == 'political':
        link = "https://g1.globo.com/politica/"

    elif seed == 'global':
        link = "https://g1.globo.com/mundo/"

    elif seed == 'daily':
        link = "https://g1.globo.com/globonews/"

    elif seed == 'economy':
        link = "https://g1.globo.com/economia/"

    elif seed == 'technology':
        link = "https://g1.globo.com/economia/tecnologia/"

    html_code = urlopen(link).read().decode("utf-8")
    html_code = html_code.split(' ')

    news = []
    for results in html_code:
        # Values of links with no contents

        if "ao-vivo" not in results and "ultimos-videos" not in results and 'podcast' not in results:
            if ".ghtml" in results:
                if results[6:-1] not in news:
                    news.append(results[6:-1])  # Place of link on html

                if len(news) >= 3:
                    break

    with open('used_newslinks.txt', 'r') as links:
        used_newslinks = links.readlines()

        for i in range(len(used_newslinks)):
            used_newslinks[i] = used_newslinks[i][0:-1]

    with open('used_newslinks.txt', 'a') as newslinks:
        for new in news:
            new2send = new
            if new not in used_newslinks:
                newslinks.write(new)
                newslinks.write('\n')
                return new2send

    return 'no news'
