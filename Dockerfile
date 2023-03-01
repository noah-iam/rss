FROM python:latest
WORKDIR /rss/rss/spider
COPY . /rss/rss/spider
ENTRYPOINT ["scrapy"]