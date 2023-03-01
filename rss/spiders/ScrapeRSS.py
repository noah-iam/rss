import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from rsshelper.helper import getUrls, prepare


class ScrapeRssSpider(scrapy.Spider):
    name = 'rss'
    allowed_domains = ['*.*']

    def start_requests(self):
        for url in getUrls():
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield prepare(post)
