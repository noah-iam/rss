import feedparser
import pymongo as pm
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import calendar
import time
import hashlib
from cleantext import clean

mongoClient = pm.MongoClient('mongodb://localhost:27017')
db = mongoClient['rss']
urls = db['google_trends_rss'].find_one()['urls']
output = db['trends-feed']

url: object


def main() -> object:
    for url in urls:
        d = feedparser.parse(url)
        for entry in d['entries']:
            link = entry['ht_news_item_url']
            title = entry['ht_news_item_title']
            snippet = entry['ht_news_item_snippet']
            pubDate = entry['published']
            text = getText(entry['ht_news_item_url'])
            dic = dict(
                _id=generateUniqueId(title, link, pubDate),
                link=link,
                title=title,
                snippet=snippet,
                pubDate=pubDate,
                text=text
            )
            output.insert_one(dic)


def getText(link):
    try:
        page = urlopen(
            Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
        html = page.read().decode('ISO-8859–1')
        soup = BeautifulSoup(html, "html.parser")
        return clean(soup.get_text())
    except:
        print(link)


def generateUniqueId(title, link, pubDate):
    data = str(title) + ' ' + str(link) + ''
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


main()
