# -*- coding: utf-8 -*-
import scrapy


from iphone_tracker.items import IPhoneItem
import datetime

class IphoneSpider(scrapy.Spider):

    name = "iPhone"
    allowed_domains = ["h2shop.vn", "hnammobile.com"]
    start_urls = [
        'https://www.h2shop.vn/iphone-7-plus-32gb-silver-black.html', #actually 128G 
        'https://www.h2shop.vn/iphone-8-plus-64gb-red.html',
        'https://www.h2shop.vn/iphone-8-plus-256gb-red.html', 
        'https://www.h2shop.vn/iphone-x-256gb-gray-lla-99.html', 

        'https://www.hnammobile.com/dien-thoai/apple-iphone-7-plus-128gb-gold.10238.html', 
        'https://www.hnammobile.com/dien-thoai/apple-iphone-8-plus-64gb-product-red-special-edition-.14363.html', 
        'https://www.hnammobile.com/dien-thoai/iphone-8-plus-256gb.12494.html', 
        'https://www.hnammobile.com/dien-thoai/iphone-x-256gb-.12496.html'
   
    ]

    def parse(self, response):
        
        if 'h2shop.vn' in response.url:
            for sel in response.xpath('//form'):
                item = IPhoneItem()
                item['shop_name'] = 'h2shop.vn'
                item['model_id'] = None
                item['model_name'] = sel.xpath(
                    '//h1[@class="ty-product-block-title"]/text()').extract_first()
                item['display_price'] = sel.xpath(
                    '//div[@class="ty-product-prices"]/div/span/span/bdi/span/text()').extract_first()
                item['pull_date'] = datetime.datetime.now()
                yield item

        elif 'hnammobile.com' in response.url:
            for sel in response.xpath('//form'):
                item = IPhoneItem()
                item['shop_name'] = 'hnammobile.com'
                item['model_id'] = None  # TODO find a product ID in the HTML
                item['model_name'] = sel.xpath(
                    '//h2[@class="title"]/text()').extract_first()
                item['display_price'] = sel.xpath(
                    '//h3[@class="price khuyenmai"]//font[@class="numberprice"]/text()').extract_first()
                item['pull_date'] = datetime.datetime.now()
                yield item
