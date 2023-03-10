from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from ScrapeRSS import ScrapeRssSpider
from rsshelper.helper import getTime
import logging
settings = get_project_settings()


def crawl_job():
    """
    Job to start spiders.
    Return Deferred, which will execute after crawl has completed.
    """
    logging.info("Crawl Job Scheduled %s", str(getTime()))
    runner = CrawlerRunner(settings)
    return runner.crawl(ScrapeRssSpider)


def schedule_next_crawl(null, sleep_time):
    """
    Schedule the next crawl
    """
    logging.info("Crawl Job Scheduled %s", str(getTime()))
    reactor.callLater(sleep_time, crawl)


def crawl():
    """
    A "recursive" function that schedules a crawl 30 seconds after
    each successful crawl.
    """
    # crawl_job() returns a Deferred
    d = crawl_job()
    # call schedule_next_crawl(<scrapy response>, n) after crawl job is complete
    d.addCallback(schedule_next_crawl, settings.get('CRAWL_TIME'))
    d.addErrback(catch_error)


def catch_error(failure):
    print(failure.value)


if __name__ == "__main__":
    crawl()
    reactor.run()
