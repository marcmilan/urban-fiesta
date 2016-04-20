# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


def serialize_model_name(value):
    return value.lstrip(' AplePLE').rstrip('TBH ')


def serialize_display_price(value):
    # dots for separators, 'VND' for currency name
    value = str(value.lstrip('HNAMCTY: ').rstrip(u'\u0111'))
    return '{} VND'.format((value).replace(',', '.'))


class IPhoneItem(scrapy.Item):

    shop_name = scrapy.Field()
    model_id = scrapy.Field()
    model_name = scrapy.Field(serializer=serialize_model_name)
    display_price = scrapy.Field(serializer=serialize_display_price)
    computable_price = scrapy.Field()
