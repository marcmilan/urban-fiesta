# -*- coding: utf-8 -*-
import scrapy


from iphone_tracker.items import IPhoneItem


class IphoneSpider(scrapy.Spider):

    name = "iPhone"
    allowed_domains = ["h2shop.vn", "hnammobile.com"]
    start_urls = [
        'http://www.h2shop.vn/dien-thoai-en/iphone/iphone-se/',
        'http://www.h2shop.vn/dien-thoai-en/iphone/iphone-6s-en/',
        'http://www.h2shop.vn/dien-thoai-en/iphone/iphone-6/',
        'http://www.h2shop.vn/dien-thoai-en/iphone/iphone-6-plus/',
        'http://www.hnammobile.com/loai-dien-thoai/apple-iphone-se.853.html',
        'http://www.hnammobile.com/loai-dien-thoai/apple-iphone-6s.759.html',
        'http://www.hnammobile.com/loai-dien-thoai/apple-iphone-6s-plus.760.html',
        'http://www.hnammobile.com/loai-dien-thoai/apple-iphone-6-.264.html',
        'http://www.hnammobile.com/loai-dien-thoai/apple-iphone-6-plus.585.html',
    ]

    def parse(self, response):

        if 'h2shop.vn' in response.url:
            for sel in response.xpath('//form'):
                item = IPhoneItem()
                item['shop_name'] = 'h2shop.vn'
                item['model_id'] = sel.xpath(
                    '@name').extract_first()
                item['model_name'] = sel.xpath(
                    'div/div/a/@title').extract_first()
                item['display_price'] = sel.xpath(
                    'div/div/div/div/div/span/span/span/text()'
                ).extract_first()
                yield item

        elif 'hnammobile.com' in response.url:
            for sel in response.xpath('//*[@id="grid"]/li'):
                item = IPhoneItem()
                item['shop_name'] = 'hnammobile.com'
                item['model_id'] = None  # TODO find a product ID in the HTML
                item['model_name'] = sel.xpath(
                    'a/h3/text()').extract_first()
                item['display_price'] = sel.xpath(
                    'a/h4/text()').extract_first()
                yield item
