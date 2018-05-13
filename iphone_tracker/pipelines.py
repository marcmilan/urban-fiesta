# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
from scrapy.xlib.pydispatch import dispatcher


class IPhonePricePipeline(object):

    def process_item(self, item, spider):
        if item['display_price']:
            return item
        else:
            raise DropItem("Missing price in %s" % item)


class ComputablePricePipeline(object):

    def process_item(self, item, spider):
        price = item['display_price'].rstrip(u'\u0111').lstrip('HNAMCTY: ')
        item['computable_price'] = int(price.replace(',', '').replace('.', ''))
        return item

class DuplicatesPipeline(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        #using model_id and shop_name as primary key for duplicates
        pk = item['model_name'] + item['shop_name']

        if (pk) in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(pk)
            return item


class JsonExportPipeline(object):

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.files = {}

    def spider_opened(self, spider):
        file = open('%s_items.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = JsonItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
