# urban-fiesta
tracking iPhone prices in the ever-changing Vietnam market

#### usage

```
scrapy crawl iPhone

or to generate a csv file of results:

scrapy crawl iPhone -o iPhone_items.csv -t csv

```



in order to use S3 for storing the json export feed, you will need to set your own AWS credentials as environment variables (see settings.py).
