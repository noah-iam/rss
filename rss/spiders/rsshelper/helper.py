import datetime

from mongo.connection import mongoConnect
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import calendar
import time
import hashlib
from scrapy.utils.project import get_project_settings
from datetime import datetime as dt

settings = get_project_settings()


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


def getTime():
    return dt.now()


def remove_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text(separator=" ")
    return stripped_text


def getCleanText(post, link):
    if "ndtv" in link :
        text = post.xpath('content:encoded//text()',
                          namespaces={'content': 'http://purl.org/rss/1.0/modules/content/'})\
            .extract_first()
        return remove_html_tags(text)
    else:
        return "NA"


def prepare(post):
    title = post.xpath('title//text()').extract_first()
    link = post.xpath('link//text()').extract_first()
    pubDate = post.xpath('pubDate//text()').extract_first()
    text = getText(link)
    cleanText = getCleanText(post, link)

    return {
        '_id': generateUniqueId(title, link, pubDate),
        'title': title,
        'link': link,
        'pubDate': pubDate,
        'raw_text': text,
        'clean_text': cleanText,
        'crawlTime': getTimeStamp()
    }


def getUrls():
    db = mongoConnect()
    coll = db[settings.get("RSS_URLS")]
    print(coll.find_one())
    dictRSS = coll.find_one()
    print(dictRSS)
    rss_urls = dictRSS[settings.get("URL_FIELD")]
    return rss_urls


def generateUniqueId(title, link, pubDate):
    data = str(title) + ' ' + str(link) + ' ' + str(pubDate) + ''
    return hashlib.sha256(data.encode('utf-8')).hexdigest()
