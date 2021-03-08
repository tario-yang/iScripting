# coding: utf-8
import scrapy

class NintendoEShopAllGames(scrapy.Spider):
    name = 'NintendoEShopAllGames'
    allowed_domains = ['nintendo.com.hk']
    start_urls = ['https://store.nintendo.com.hk/games/all-released-games']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request('{0}'.format(url))

    def parse(self, response):
        def cleanFormat(data):
            return data.strip()

        def formatReleasedData(data):
            return '20{0}/{1}/{2}'.format(data[0],data[1],data[2])

        self.resultSet = []

        for game in response.css('.category-product-item'):
            self.resultSet.append({
                'image': game.css('.category-product-item-img img').attrib['data-src'],
                'name': cleanFormat(game.css('.category-product-item-title a::text').get()),
                'price': game.css('.category-product-item-price .price::text').get(),
                'release': formatReleasedData(game.css('.category-product-item-released').re('[0-9]{1,}')),
                'details': game.css('.category-product-item-img a').attrib['href']
            })

        return self.resultSet
