# coding: utf-8
import scrapy
from datetime import datetime


class NintendoEShopSale(scrapy.Spider):
    name = 'NintendoEShopSale'
    allowed_domains = ['nintendo.com.hk']
    start_urls = ['https://store.nintendo.com.hk/games/sale']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request('{0}'.format(url))

    def parse(self, response):
        def formatReleasedData(data):
            return '20{0}/{1}/{2}'.format(data[0],data[1],data[2])

        def getPrice(data):
            return float(data.split(' ')[1])

        print('当前时间：{0}\n数据源自：{1}\n\n检索折扣表单>>>\n'.format(datetime.now(), self.start_urls[0]))

        for game in response.css('.category-product-item'):
            oldPrice = game.css('.category-product-item-price .old-price .price::text').get()
            specialPrice = game.css('.category-product-item-price .special-price .price::text').get()
            discountRate = format(getPrice(specialPrice)/getPrice(oldPrice)*100, '.2f')

            yield {
                'image': game.css('.category-product-item-img img').attrib['data-src'],
                'name': game.css('.category-product-item-title a::text').get().strip(),
                'old_price': oldPrice,
                'special_price': specialPrice,
                'discount': '{0}%'.format(discountRate),
                'release': formatReleasedData(game.css('.category-product-item-released').re('[0-9]{1,}'))
            }
