import os
import urllib
from configparser import ConfigParser
from pathlib import Path
import pymongo as pm
from scrapy.utils.project import get_project_settings
import pymongo

parser = ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
home = str(Path.home())

settings = get_project_settings()


def mongoConnect():
    print("connecting to mongo")
    try:
        client = pm.MongoClient(settings.get("MONGO_URI"))
        database = client[settings.get("MONGO_DATABASE")]
        return database
    except ex:
        print("error in ̰ connecting", ex)