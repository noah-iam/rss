import pymongo as pm

settings = get_project_settings()

mongoClient = pm.MongoClient(settings.get("MONGO_URI"))
db = mongoClient[settings.get("MONGO_DATABASE")]


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
                "https://indianexpress.com/syndication/",
                "https://www.thehindu.com/rss/feeds/",
                "https://feeds.feedburner.com/ndtvnews-india-news",
                "https://timesofindia.indiatimes.com/rss.cms",
                "https://www.indiatoday.in/rss/home",
                "https://www.hindustantimes.com/rss",
                "https://indianexpress.com/feed/",
                "https://zeenews.india.com/rss/india-national-news.xml",
                "https://www.news18.com/rss/india.xml",
                "https://www.business-standard.com/rss/latest-news",
                "https://economictimes.indiatimes.com/rssfeedsdefault.cms"
            ]
        }
        )


main()
