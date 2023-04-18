import pymongo as pm

mongoClient = pm.MongoClient('mongodb://localhost:27017')
db = mongoClient['rss']


def main():
    insert_GtrendsUrls()
    insert_RSSUrls()


def insert_GtrendsUrls():
    if db['google_trends_rss'].find_one() is None:
        print("No coll found with name: google_trends_rss ")
        db['google_trends_rss'].insert_one({
            "type": "GOOGLE_TRENDS",
            "urls": [
                "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IN",
                "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
            ]
        }
        )


def insert_RSSUrls():
    if db['rss-url'].find_one() is None:
        print("No coll found with name: rss-url ")
        db['rss-url'].insert_one({
            "type": "NEWS",
            "urls": [
                "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
                "https://www.thehindu.com/news/national/feeder/default.rss",
                "https://feeds.feedburner.com/ndtvnews-india-news",
                "https://timesofindia.indiatimes.com/rssfeedmostrecent.cms",
                "https://www.indiatoday.in/rss/home",
                "https://indianexpress.com/feed/",
                "https://zeenews.india.com/rss/india-national-news.xml",
                "https://www.news18.com/rss/india.xml",
                "https://www.business-standard.com/rss/home_page_top_stories.rss",
                "https://www.business-standard.com/rss/latest.rss",
                "https://economictimes.indiatimes.com/rssfeedsdefault.cms"
            ]
        }
        )


main()
