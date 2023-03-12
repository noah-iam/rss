FROM python:3.7

RUN mkdir /rss
WORKDIR /rss/
ADD . /rss/
ADD start.sh /

RUN pip install -r requirements.txt

RUN chmod +x /start.sh

CMD ["/start.sh"]