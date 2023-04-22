# Setup Project
## Dependencies
1. > pip install pymongo
2. > pip install scrapy
3. > pip install < Name of the Module if missing >

## setup using conda environment 

1. Add the conda-forge channel to your Conda configuration:
conda config --add channels conda-forge

2. Create a new Conda environment with the name daily and install the required packages from requirements.txt:

conda create --name daily --file requirements.txt

3. 
conda activate daily
pip install clean-text==0.6.0
pip install selenium==4.8.0

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

## To update tag name of image

1. docker-compose build 
2.  docker-compose up 
3. docker tag rss-rss:latest pratikbtn/rss-rss:latest 
4. docker push pratikbtn/rss-rss


## Reference
> https://doc.scrapy.org/en/latest/index.html

## launch.json 

{
    "version": "0.2.0",
    "configurations": [
    

        {
            "name": "Debug crawler.py",
            "type": "python",
            "request": "launch",
            "program": "rss/spiders/crawler.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        }
    ]
}

