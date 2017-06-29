# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from tc_zufang.utils.result_parse import list_first_item
from scrapy.http import Request
from tc_zufang.items import TcZufangItem
import re
defaultencoding = 'utf-8'
'''
58同城的爬虫
'''
#继承自RedisSpider，则start_urls可以从redis读取
#继承自BaseSpider，则start_urls需要写出来
class TczufangSpider(RedisSpider):
    name='tczufang'
    redis_key = 'tczufang_tc:requests'
    #解析从start_urls下载返回的页面
    #页面页面有两个目的：
    #第一个：解析获取下一页的地址，将下一页的地址传递给爬虫调度器，以便作为爬虫的下一次请求
    #第二个：获取详情页地址，再对详情页进行下一步的解析
    #对详情页进行下一步的解析
    def parse(self, response):
        tczufangItem=TcZufangItem()
        response_url = re.findall('^http\:\/\/\w+\.58\.com', response.url)
        response_selector = Selector(response)
        # 字段的提取可以使用在终端上scrapy shell进行调试使用
        # 帖子名称
        raw_title=list_first_item(response_selector.xpath(u'//div[contains(@class,"house-title")]/h1[contains(@class,"c_333 f20")]/text()').extract())
        if raw_title:
            tczufangItem['title'] =raw_title.encode('utf8')
        #t帖子发布时间,进一步处理
        raw_time=list_first_item(response_selector.xpath(u'//div[contains(@class,"house-title")]/p[contains(@class,"house-update-info c_888 f12")]/text()').extract())
        try:
            tczufangItem['pub_time'] =re.findall(r'\d+\-\d+\-\d+\s+\d+\:\d+\:\d+',raw_time)[0]
        except:
            tczufangItem['pub_time']=0
        #租金
        tczufangItem['money']=list_first_item(response_selector.xpath(u'//div[contains(@class,"house-pay-way f16")]/span[contains(@class,"c_ff552e")]/b[contains(@class,"f36")]/text()').extract())
        # 租赁方式
        raw_method=list_first_item(response_selector.xpath(u'//ul[contains(@class,"f14")]/li[1]/span[2]/text()').extract())
        try:
            tczufangItem['method'] =raw_method.encode('utf8')
        except:
            tczufangItem['method']=0
        # 所在区域
        try:
            area=response_selector.xpath(u'//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[1]
        except:
            area=''
        if area:
            area=area
        try:
            area2=response_selector.xpath(u'//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[2]
        except:
            area2=''
        raw_area=area+"-"+area2
        if raw_area:
            raw_area=raw_area.encode('utf8')
        tczufangItem['area'] =raw_area if raw_area else None
        # 所在小区
        try:
            raw_community = response_selector.xpath(u'//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[0]
            if raw_community:
                raw_community=raw_community.encode('utf8')
            tczufangItem['community']=raw_community if raw_community else None
        except:
            tczufangItem['community']=0
        # 帖子详情url
        tczufangItem['targeturl']=response.url
        #帖子所在城市
        tczufangItem['city']=response.url.split("//")[1].split('.')[0]
        #帖子的联系电话
        try:
            tczufangItem['phone']=response_selector.xpath(u'//div[contains(@class,"house-fraud-tip")]/span[1]/em[contains(@class,"phone-num")]/text()').extract()[0]
        except:
            tczufangItem['phone']=0
        # 图片1的联系电话
        try:
            tczufangItem['img1'] = response_selector.xpath(u'//ul[contains(@class,"pic-list-wrap pa")]/li[1]/@data-src').extract()[0]
        except:
            tczufangItem['img1'] = 0
        # 图片1的联系电话
        try:
            tczufangItem['img2'] = response_selector.xpath(u'//ul[contains(@class,"pic-list-wrap pa")]/li[2]/@data-src').extract()[0]
        except:
             tczufangItem['img2'] = 0
        yield tczufangItem