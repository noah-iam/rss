import os
import urllib
from configparser import ConfigParser
from pathlib import Path

import pymongo

parser = ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
home = str(Path.home())


def get_conn_str():
    HOST = parser.get("Default", "DB_HOST")
    PORT = parser.get('Default', 'DB_PORT')
    USER_NAME = parser.get('Default', 'DB_USER')
    PASSWORD = parser.get('Default', 'DB_PWD')
    #return "mongodb://root:rootpassword@localhost:27017/admin?authSource=rss"
    return "mongodb://" + USER_NAME + ':' + urllib.parse.quote(PASSWORD) + "@" + HOST + ":" + str(PORT)


def mongoConnect():
    DB_SCHEMA = parser.get('Default', 'DB_SCHEMA')
    client = pymongo.MongoClient(get_conn_str())
    database = client[DB_SCHEMA]
    return database
