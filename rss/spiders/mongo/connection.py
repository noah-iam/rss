import os
import urllib
from configparser import ConfigParser
from pathlib import Path
import pymongo

import pymongo

parser = ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
home = str(Path.home())


def mongoConnect():
    client = pymongo.MongoClient('mongodb://root:rootpassword@localhost:27017')
    database = client['rss']
    return database
