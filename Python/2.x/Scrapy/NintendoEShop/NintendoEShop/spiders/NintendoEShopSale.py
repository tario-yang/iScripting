# coding: utf-8
import scrapy
from datetime import datetime
from logger import logger


class NintendoEShopSale(scrapy.Spider):
    name='Sale'
    allowed_domains=['nintendo.com.hk']
    start_urls=['https://store.nintendo.com.hk/games/sale']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request('{0}'.format(url))

    def parse(self, response):
        def formatReleasedData(data):
            return '20{0}/{1}/{2}'.format(data[0],data[1],data[2])

        logger.info('Start to fetch data from {0}...'.format(self.start_urls[0]))

        print('当前时间：{0}\n数据源自：{1}\n\n检索折扣表单...\n'.format(datetime.now(), self.start_urls[0]))

        resultSet={}
        count=1
        for game in response.css('.category-product-item'):
            oldPrice=game.css(
                '.category-product-item-price .old-price .price::text').get().replace('HKD ', '')
            specialPrice=game.css(
                '.category-product-item-price .special-price .price::text').get().replace('HKD ', '')
            discountRate=str(format(float(specialPrice)/float(oldPrice), '.2f'))

            resultSet[str(count)]={
                'image': game.css('.category-product-item-img img').attrib['data-src'],
                'name': game.css('.category-product-item-title a::text').get().strip(),
                'old_price': oldPrice,
                'special_price': specialPrice,
                'discount': discountRate,
                'release': formatReleasedData(game.css('.category-product-item-released').re('[0-9]{1,}'))
            }
            count+=1

        yield resultSet

        print('检索结束。')
