# coding: utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import timezone, datetime, date
import json
from pyecharts.charts import Bar, Line
from pyecharts import options as opts


class NintendoeshopPipelineTimeStamp:
    def process_item(self, item, spider):
        if spider.name == "AllGames":
            item['crawlDate'] = datetime.now(timezone.utc).isoformat()

class NintendoeshopPipelineDisplayData:
    def process_item(self, item, spider):
        if spider.name == 'Sale':
            for i in item:
                print(''' * 名称：{0} ({1})\n\t价格（折扣后）：{2}\n\t价格（折扣前）：{3}\n\t价格（折扣率）：{4}
                      '''.format(
                            item[i]['name'],
                            item[i]['release'],
                            item[i]['special_price'],
                            item[i]['old_price'],
                            item[i]['discount']))

        if spider.name == "AllGames":
            for i in item:
                print(''' * 名称：{0} ({1})\n\t图片：{2}\n\t价格：{3}\n\t详细：{4}
                    '''.format(
                            item[i]['name'],
                            item[i]['release'],
                            item[i]['image'],
                            item[i]['price'],
                            item[i]['details']))

        return item

class NintendoeshopPipelineSave2File:
    def process_item(self, item, spider):
        with open('dataOutput_{0}.json'.format(spider.name), 'a+') as f:
            json.dump(item, f, ensure_ascii=False, indent=2)

        return item

class NintendoeshopPipelineShowChart:

    def process_item(self, item, spider):

        def formatData4Sale():
            return [(
                item[i]['name'],
                item[i]['special_price'],
                item[i]['old_price'],
                item[i]['discount']
            ) for i in item]

        def getNameData4Sale(data):
            return [i[0] for i in data]

        def getSPriceData4Sale(data):
            return [i[1] for i in data]

        def getOPriceData4Sale(data):
            return [i[2] for i in data]

        def getDiscountDate4Sale(data):
            return [i[3] for i in data]

        def formatData4AllGames():
            return [(
                item[i]['name'],
                item[i]['price'],
            ) for i in item]

        def getNameData4AllGames(data):
            return [i[0] for i in data]

        def getSPriceData4AllGames(data):
            return [i[1] for i in data]

        def SaleChart():
            data=formatData4Sale()
            chartBar=(
                Bar(
                    init_opts=opts.InitOpts(
                        width='1200px',
                        height='600px',
                        page_title='On Sale List',
                        animation_opts=opts.AnimationOpts(
                            animation_delay=1000, animation_easing="elasticOut"
                        ),
                ))
                .add_xaxis(getNameData4Sale(data))
                .add_yaxis(
                    series_name='限时（HKD）',
                    y_axis=getSPriceData4Sale(data),
                )
                .add_yaxis(
                    series_name='原价（HKD）',
                    y_axis=getOPriceData4Sale(data),
                )
                .extend_axis(
                    yaxis=opts.AxisOpts(
                        name='折扣率',
                        type_='value',
                        min_=0,
                        max_=1,
                        interval=0.5,
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    )
                )
                .set_global_opts(
                    title_opts=opts.TitleOpts(
                        title='任天堂港服折扣游戏',
                        title_link=spider.start_urls[0],
                        subtitle='({0})'.format(date.today()),
                    ),
                    tooltip_opts=opts.TooltipOpts(
                        is_show=True,
                        trigger="axis",
                        axis_pointer_type="cross",
                    ),
                    xaxis_opts=opts.AxisOpts(
                        type_="category",
                        axispointer_opts=opts.AxisPointerOpts(
                            is_show=True,
                            type_="shadow"
                        ),
                        axislabel_opts=opts.LabelOpts(rotate=-10)
                    ),
                    yaxis_opts=opts.AxisOpts(
                        name="",
                        type_="value",
                        min_=0,
                        max_=800,
                        interval=200,
                        axislabel_opts=opts.LabelOpts(formatter="HKD {value}"),
                        axistick_opts=opts.AxisTickOpts(is_show=True),
                        splitline_opts=opts.SplitLineOpts(is_show=True),
                    ),
                )
            )

            chartLine=(
                Line()
                .add_xaxis(getNameData4Sale(data))
                .add_yaxis(
                    series_name='折扣率',
                    yaxis_index=1,
                    y_axis=getDiscountDate4Sale(data),
                    label_opts=opts.LabelOpts(is_show=False),
                )
            )

            return chartBar.overlap(chartLine)

        def AllGamesChart():
            data=formatData4AllGames()
            chartBar=(
                Bar(
                    init_opts=opts.InitOpts(
                        width='2000px',
                        height='8000px',
                        page_title='All Games List',
                    ))
                .add_xaxis(getNameData4AllGames(data))
                .add_yaxis(
                    series_name='',
                    y_axis=getSPriceData4AllGames(data),
                    category_gap="30%"
                )
                .reversal_axis()
                .set_series_opts(
                    label_opts=opts.LabelOpts(
                        position='right',
                        font_weight='bold',
                        formatter='HKD {c}'
                    ),
                    markpoint_opts=opts.MarkPointOpts(
                        data=[
                            opts.MarkPointItem(type_="max", name="最大值"),
                            # opts.MarkPointItem(type_="min", name="最小值"),
                            # opts.MarkPointItem(type_="average", name="平均值"),
                        ]
                    ),
                )
                .set_global_opts(
                    title_opts=opts.TitleOpts(
                        title='任天堂港服游戏',
                        title_link=spider.start_urls[0],
                        subtitle='({0})'.format(date.today()),
                    )
                )
            )

            return chartBar

        if spider.name == 'Sale':
            SaleChart().render('sale_report.html')

        if spider.name == 'AllGames':
            AllGamesChart().render('all_game_report.html')
