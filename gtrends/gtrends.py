import feedparser
import pymongo as pm
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import hashlib
from cleantext import clean

mongoClient = pm.MongoClient('mongodb://localhost:27017')
db = mongoClient['rss']
urls = db['google_trends_rss'].find_one()['urls']
collection = db['trends-feed']

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
            document = dict(
                _id=generateUniqueId(title, link, pubDate),
                link=link,
                title=title,
                snippet=snippet,
                pubDate=pubDate,
                text=text
            )

            if collection.count_documents({"_id": document["_id"]}) == 0:
                collection.insert_one(document)
            else:
                print("Document with _id: {} already exists".format(
                    document["_id"]))


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
