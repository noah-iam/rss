from rss.spiders.mongo.connection import mongoConnect
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import calendar
import time
import hashlib


def getText(link):
    page = urlopen(
        Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


def getTimeStamp():
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    return time_stamp


def prepare(post):
    title = post.xpath('title//text()').extract_first()
    link = post.xpath('link//text()').extract_first()
    pubDate = post.xpath('pubDate//text()').extract_first()
    text = getText(post.xpath('link//text()').extract_first())

    return {
        '_id': generateUniqueId(title, link, pubDate),
        'title': title,
        'link': link,
        'pubDate': pubDate,
        'text': text,
        'crawlTime': getTimeStamp()
    }


def getUrls():
    db = mongoConnect()
    coll = db['rss-url']
    dictRSS = coll.find_one()
    rss_urls = dictRSS['urls']
    return rss_urls


def generateUniqueId(title, link, pubDate):
    data = str(title) + ' ' + str(link) + ' ' + str(pubDate) + ''
    return hashlib.sha256(data.encode('utf-8')).hexdigest()
