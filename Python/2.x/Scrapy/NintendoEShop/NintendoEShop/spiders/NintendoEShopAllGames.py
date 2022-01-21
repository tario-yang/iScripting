# coding: utf-8
import scrapy
from logger import logger

class NintendoEShopAllGames(scrapy.Spider):
    name='AllGames'
    allowed_domains=['nintendo.com.hk']
    start_urls = [
        'https://store.nintendo.com.hk/games/all-released-games?product_list_order=price_desc']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request('{0}'.format(url))

    def parse(self, response):
        def cleanFormat(data):
            return data.strip()

        def formatReleasedData(data):
            return '20{0}/{1}/{2}'.format(data[0],data[1],data[2])

        logger.info('Start to fetch data from {0}...'.format(self.start_urls[0]))

        resultSet={}
        count=1
        for game in response.css('.category-product-item'):
            resultSet[str(count)]={
                'image': game.css('.category-product-item-img img').attrib['data-src'],
                'name': cleanFormat(game.css('.category-product-item-title a::text').get()),
                'price': game.css('.category-product-item-price .price::text').get().replace('HKD ', ''),
                'release': formatReleasedData(game.css('.category-product-item-released').re('[0-9]{1,}')),
                'details': game.css('.category-product-item-img a').attrib['href']
            }
            count+=1

        yield resultSet
