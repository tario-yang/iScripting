# coding: utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import timezone, datetime
import json
import logging

logger = logging.getLogger(__name__)

class NintendoeshopPipelineTimeStamp:
    def process_item(self, item, spider):
        item['crawlDate'] = datetime.now(timezone.utc).isoformat()
        return item

class NintendoeshopPipeline:
    def process_item(self, item, spider):
        if spider.name == 'NintendoEShopSale':
            print(''' * 名称：{0} ({1})
            价格（折扣后）：{2}
            价格（折扣前）：{3}
            价格（折扣率）：{4}
            '''.format(item['name'],
                    item['release'],
                    item['special_price'],
                    item['old_price'],
                    item['discount']))

        if spider.name == "NintendoEShopAllGames":
            print(''' * 名称：{0} ({1})
            图片：{2}
            价格：{3}
            详细：{4}
            '''.format(item['name'],
                    item['release'],
                    item['image'],
                    item['price'],
                    item['details']))

        return item

class NintendoeshopPipelineSave2File:
    def process_item(self, item, spider):
        with open('dataOutput_{0}.json'.format(spider.name), 'a+') as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
            logger.info('Data is saved to "{0}.txt".'.format(spider.name))

        return item