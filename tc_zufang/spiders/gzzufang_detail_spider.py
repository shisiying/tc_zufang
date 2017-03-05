# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tc_zufang.utils.result_parse import list_first_item
from scrapy.http import Request
from tc_zufang.items import TcZufangItem
import re
defaultencoding = 'utf-8'
'''
赶集网的爬虫
'''
#继承自RedisSpider，则start_urls可以从redis读取
#继承自BaseSpider，则start_urls需要写出来
class TczufangSpider(BaseSpider):
    name='gzzufang'
    start_urls=(
        'http://dg.ganji.com/fang1/',
        'http://sw.ganji.com/fang1/',
    )
    # redis_key = 'tczufangCrawler:start_urls'
    #解析从start_urls下载返回的页面
    #页面页面有两个目的：
    #第一个：解析获取下一页的地址，将下一页的地址传递给爬虫调度器，以便作为爬虫的下一次请求
    #第二个：获取详情页地址，再对详情页进行下一步的解析
    def parse(self, response):
        #获取所访问的地址
        response_url = re.findall('^http\:\/\/\w+\.ganji\.com', response.url)[0]
        response_selector = Selector(response)
        next_link=response_selector.xpath(u'//ul[contains(@class,"pageLink clearfix")]/li/a[contains(@class,"next")]/@href').extract()[0]
        if next_link:
            yield Request(url=response_url+next_link, callback=self.parse)
        for detail_link in response_selector.xpath(u'//dl[contains(@class,"f-list-item-wrap f-clear")]/dd[contains(@class,"dd-item title")]/a/@href').extract():
            detail_link = response_url + detail_link
           #对详情页进行解析
            if detail_link:
               yield Request(url=detail_link, callback=self.parse_detail)
    # 对详情页进行下一步的解析
    def parse_detail(self, response):
        tczufangItem=TcZufangItem()
        response_selector = Selector(response)
        # 字段的提取可以使用在终端上scrapy shell进行调试使用
        # 帖子名称
        raw_title=list_first_item(response_selector.xpath(u'//div[contains(@class,"card-top")]/p[contains(@class,"card-title")]/i/text()').extract())
        tczufangItem['title'] =raw_title
        # #t帖子发布时间,进一步处理
        tczufangItem['pub_time'] =None
        #租金
        money=list_first_item(response_selector.xpath(u'//div[contains(@class,"card-top")]/ul[contains(@class,"card-pay f-clear")]/li[contains(@class,"price")]/span[contains(@class,"num")]/text()').extract())
        if money:
            money=money.encode('utf8')
        tczufangItem['money']=money
        # 租赁方式
        raw_method=list_first_item(response_selector.xpath(u'//div[contains(@class,"fang-info")]/span[2]/text()').extract())
        if raw_method:
            raw_method=raw_method.encode("utf8");
        tczufangItem['method'] =raw_method
        # 所在区域
        area=response_selector.xpath(u'//div[contains(@class,"card-item f-clear")][2]/p/span/a[1]/text()').extract()[0]
        area+='-'+response_selector.xpath(u'//div[contains(@class,"card-item f-clear")]/p/span/a[2]/text()').extract()[0]
        area1=response_selector.xpath(u'//div[contains(@class,"card-item f-clear")]/p/span/a[3]/text()').extract()
        if area1:
            area=area+'-'+area1[0]
        if area:
            area=area.encode("utf8");
        tczufangItem['area'] =area
        # 所在小区
        raw_community =list_first_item(response_selector.xpath(u'//div[contains(@class,"card-item f-clear")]/p/span/text()').extract())
        if raw_community.strip():
            raw_community=raw_community.strip().encode('utf8')
            tczufangItem['community'] = raw_community
        else:
            raw_community = list_first_item(response_selector.xpath(u'//div[contains(@class,"card-item f-clear")]/p/span[1]/a/text()').extract())
            tczufangItem['community'] = raw_community

        # 帖子详情url
        tczufangItem['targeturl']=response.url
        # #帖子所在城市
        tczufangItem['city']=response.url.split("//")[1].split('.')[0]
        yield tczufangItem