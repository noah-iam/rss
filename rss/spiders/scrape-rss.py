import scrapy


class ScrapeRssSpider(scrapy.Spider):
    name = 'scrape-rss'
    allowed_domains = ['https://www.blog.google/rss']
    start_urls = ['http://https://www.blog.google/rss/']

    def start_requests(self):
        urls = [
            'https://www.blog.google/rss',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.xpath('//channel/item'):
            yield {
                'title' : post.xpath('title//text()').extract_first(),
                'link': post.xpath('link//text()').extract_first(),
                'pubDate' : post.xpath('pubDate//text()').extract_first(),
            }