***To Run Scrapy RSS:***

** Update Mongo Connection:**
1. Go to rss/rss/settings.py
2. Change the Mongo URI as per your MONGO DB URI

**To  change crawl frequency :**
1. go to rss/rss/settings.py
2. update 
   3. CRAWL_TIME = 300 in Second ( You can Update)

**To Run the Scrapy :**

1. go to rss/spiders/crawler.py
2. Run the command in terminal 
   3. *python crawl.py*



