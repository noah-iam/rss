# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from rss.spiders.mongo.connection import mongoConnect


class RssPipeline:
    def __init__(self):
        db = mongoConnect()
        coll = db['rss-feed']
        self.collection = coll

    def process_item(self, item, spider):
        self.collection.insert_one(item)
        return item
