# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tc_zufang.utils.result_parse import list_first_item
from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider
from tc_zufang.items import TcZufangItem
import re
'''
58同城的爬虫
'''
#继承自RedisSpider，则start_urls可以从redis读取
#继承自BaseSpider，则start_urls需要写出来
class TczufangSpider(RedisSpider):
    name='tczufang'
    # start_urls=(
    #     'http://dg.58.com/chuzu/',
    #     'http://sw.58.com/chuzu/',
    # )
    redis_key = 'tczufangCrawler:start_urls'
    #解析从start_urls下载返回的页面
    #页面页面有两个目的：
    #第一个：解析获取下一页的地址，将下一页的地址传递给爬虫调度器，以便作为爬虫的下一次请求
    #第二个：获取详情页地址，再对详情页进行下一步的解析
    def parse(self, response):
        #获取所访问的地址
        response_url=re.findall('^http\:\/\/\w+\.58\.com',response.url)
        response_selector = Selector(response)
        next_link=list_first_item(response_selector.xpath(u'//div[contains(@class,"pager")]/a[contains(@class,"next")]/@href').extract())
        if next_link:
            # print next_link
            yield Request(url=next_link, callback=self.parse)
        for detail_link in response_selector.xpath(u'//div[contains(@class,"listBox")]/ul[contains(@class,"listUl")]/li/@logr').extract():
         #gz_2_39755299868183_28191154595392_sortid:1486483205000 @ ses:busitime ^ desc @ pubid:5453707因为58同城的详情页做了爬取限制，所以由自己构造详情页id
         #构造详情页url
           # detail_link='http://dg.58.com/zufang/'+detail_link.split('_')[3]+'x.shtml'
           detail_link = response_url[0]+'/zufang/' + detail_link.split('_')[3] + 'x.shtml'
           #对详情页进行解析
           if detail_link:
               yield Request(url=detail_link, callback=self.parse_detail)
    #对详情页进行下一步的解析
    def parse_detail(self, response):
        tczufangItem=TcZufangItem()
        response_selector = Selector(response)
        # 字段的提取可以使用在终端上scrapy shell进行调试使用
        # 帖子名称
        raw_title=list_first_item(response_selector.xpath(u'//div[contains(@class,"house-title")]/h1[contains(@class,"c_333 f20")]/text()').extract())
        tczufangItem['title'] =raw_title.encode('utf8')
        #t帖子发布时间,进一步处理
        raw_time=list_first_item(response_selector.xpath(u'//div[contains(@class,"house-title")]/p[contains(@class,"house-update-info c_888 f12")]/text()').extract())
        tczufangItem['pub_time'] =re.findall(r'\d+\-\d+\-\d+\s+\d+\:\d+\:\d+',raw_time)[0]
        #租金
        tczufangItem['money']=list_first_item(response_selector.xpath(u'//div[contains(@class,"house-pay-way f16")]/span[contains(@class,"c_ff552e")]/b[contains(@class,"f36")]/text()').extract())
        # 租赁方式
        raw_method=list_first_item(response_selector.xpath(u'//ul[contains(@class,"f14")]/li[1]/span[2]/text()').extract())
        tczufangItem['method'] =raw_method.encode('utf8')
        # 所在区域
        raw_area=response_selector.xpath(u'//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[1].encode('utf8')+"-"+response_selector.xpath(u'//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[2].encode('utf8')
        tczufangItem['area'] =raw_area if raw_area else None
        # 所在小区
        raw_community = response_selector.xpath(u'//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[0].encode('utf8')
        tczufangItem['community']=raw_community if raw_community else None
        # 帖子详情url
        tczufangItem['targeturl']=response.url
        #帖子所在城市
        tczufangItem['city']=response.url.split("//")[1].split('.')[0]
        yield tczufangItem