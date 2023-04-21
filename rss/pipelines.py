# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from pymongo.errors import DuplicateKeyError


class RssPipeline:

    def __init__(self, mongo_uri, mongo_db, collection_name, rss_url):
        self.db = None
        self.client = None
        self.urls = None
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name
        self.rss_url = rss_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            collection_name=crawler.settings.get("RSS_DATA"),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            rss_url=crawler.settings.get("RSS_DATA")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.urls = self.db.get_collection(self.rss_url)['urls']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        try:
            if self.db[self.collection_name].count_documents({"_id": item["_id"]}) == 0:
                self.db[self.collection_name].insert_one(item)
            else:
                print("Document with _id: {} already exists".format(
                    item["_id"]))
        except DuplicateKeyError as e:
            print("Error: Duplicate key - {}".format(e.details))
        return item
