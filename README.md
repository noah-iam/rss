# Setup Project
## Dependencies
1. > pip install pymongo
2. > pip install scrapy
3. > pip install < Name of the Module if missing >
   

# Run Scrapy RSS

## Update Mongo Connection:
1. Go to rss/rss/settings.py
2. Change the Mongo URI as per your MONGO DB URI

## To  change crawl frequency :
1. Go to rss/rss/settings.py]
2. update CRAWL_TIME = 300 (In Seconds)

## To Run the Scrapy

1. Go to rss/spiders
2. Run the command in terminal 
  > python crawl.py


## Reference
> https://doc.scrapy.org/en/latest/index.html


