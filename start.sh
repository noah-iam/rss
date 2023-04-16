#!/bin/bash
python setupDB.py
#python gtrends/gtrends.py &
python rss/spiders/crawler.py
