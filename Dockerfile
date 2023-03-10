FROM python:3.7

RUN mkdir /rss
WORKDIR /rss/
ADD . /rss/
RUN pip install -r requirements.txt
CMD ["python", "rss/spiders/crawler.py"]