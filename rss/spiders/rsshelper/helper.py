import datetime
import re
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
    try:
        if "ndtv" in link:
            text = post.xpath('content:encoded//text()',
                              namespaces={'content': 'http://purl.org/rss/1.0/modules/content/'}) \
                .extract_first()
            return remove_html_tags(text)
        if "timesofindia" in link:
            page = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div', {'class': '_s30J'}).text.strip()
            return div_text
        if "indiatoday" in link:
            page = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div',
                                 {'class': 'jsx-99cc083358cc2e2d Story_description__fq_4S description'}).text.strip()
            return div_text
        if "indianexpress" in link:
            page = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div', {'id': 'pcl-full-content'}).text.strip()
            return div_text
        if "zeenews" in link:
            page = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div', {'class': 'article_content article_description'}).text.strip()
            return div_text
        if "news18" in link:
            page = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div', {'class': 'jsx-1866577923'}).text.strip()
            return div_text
        if "business-standard" in link:
            page = urlopen(Request(link, headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div', {'class': 'storycontent'}).text.strip()
            return div_text
        if "economictimes" in link:
            page = urlopen(Request("link", headers={'User-Agent': 'Mozilla/5.0'}))
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            div_text = soup.find('div', {'class': 'artText'}).text.strip()
            return div_text
        else:
            return "NA"
    except Exception as ex:
        print(ex, link)
        return "NA"


def getDescription(post, link):
    try:
        return remove_html_tags(post.xpath('description//text()').extract_first()).strip()
    except Exception as ex:
        print(ex, link)
        return "NA"


def prepare(post):
    title = post.xpath('title//text()').extract_first()
    link = post.xpath('link//text()').extract_first()
    pubDate = post.xpath('pubDate//text()').extract_first()
    description = getDescription(post, link)
    cleanText = getCleanText(post, link)

    return {
        '_id': generateUniqueId(title, link, pubDate),
        'title': title,
        'link': link,
        'pubDate': pubDate,
        'description': description,
        'clean_text': cleanText,
        'crawlTime': getTimeStamp()
    }


def getUrls():
    db = mongoConnect()
    coll = db[settings.get("RSS_URLS")]
    dictRSS = coll.find_one()
    rss_urls = dictRSS[settings.get("URL_FIELD")]
    return rss_urls


def generateUniqueId(title, link, pubDate):
    data = str(title) + ' ' + str(link) + ' ' + str(pubDate) + ''
    return hashlib.sha256(data.encode('utf-8')).hexdigest()
