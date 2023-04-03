import scrapy
import json
from pydispatch import dispatcher
from scrapy import signals
import sys


class Base_Class(scrapy.Spider):
    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.products = []
        

    def spider_closed(self, spider):
        stats = self.crawler.stats.get_stats()
        print(json.dumps(
            {"products": self.products, "stats": stats}, default=str))
        sys.stdout.flush()
