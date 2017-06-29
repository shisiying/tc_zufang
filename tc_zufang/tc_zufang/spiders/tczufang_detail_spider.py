# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
from tc_zufang.utils.result_parse import list_first_item
from scrapy.http import Request
from tc_zufang.utils.InsertRedis import inserintotc,inserintota
import re
defaultencoding = 'utf-8'
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
    #     'http://sz.58.com/chuzu/',
    #     'http://gz.58.com/chuzu/',
    #     'http://fs.58.com/chuzu/',
    #     'http://zs.58.com/chuzu/',
    #     'http://zh.58.com/chuzu/',
    #     'http://huizhou.58.com/chuzu/',
    #     'http://jm.58.com/chuzu/',
    #     'http://st.58.com/chuzu/',
    #     'http://zhanjiang.58.com/chuzu/',
    #     'http://zq.58.com/chuzu/',
    #     'http://mm.58.com/chuzu/',
    #     'http://jy.58.com/chuzu/',
    #     'http://mz.58.com/chuzu/',
    #     'http://qingyuan.58.com/chuzu/',
    #     'http://yj.58.com/chuzu/',
    #     'http://sg.58.com/chuzu/',
    #     'http://heyuan.58.com/chuzu/',
    #     'http://yf.58.com/chuzu/',
    #     'http://chaozhou.58.com/chuzu/',
    #     'http://taishan.58.com/chuzu/',
    #     'http://yangchun.58.com/chuzu/',
    #     'http://sd.58.com/chuzu/',
    #     'http://huidong.58.com/chuzu/',
    #     'http:// boluo.58.com/chuzu/',
    # )
    # redis_key = 'tczufangCrawler:start_urls'
    #解析从start_urls下载返回的页面
    #页面页面有两个目的：
    #第一个：解析获取下一页的地址，将下一页的地址传递给爬虫调度器，以便作为爬虫的下一次请求
    #第二个：获取详情页地址，再对详情页进行下一步的解析
    redis_key = 'start_urls'
    def parse(self, response):
        #获取所访问的地址
        response_url=re.findall('^http\:\/\/\w+\.58\.com',response.url)
        response_selector = Selector(response)
        next_link=list_first_item(response_selector.xpath(u'//div[contains(@class,"pager")]/a[contains(@class,"next")]/@href').extract())
        detail_link=response_selector.xpath(u'//div[contains(@class,"listBox")]/ul[contains(@class,"listUl")]/li/@logr').extract()

        if next_link:
            if detail_link:
                    # print next_link
                # yield Request(next_link,callback=self.parse)
                inserintotc(next_link, 1)
                print '#########[success] the next link ' + next_link + ' is insert into the redis queue#########'
        for detail_link in response_selector.xpath(u'//div[contains(@class,"listBox")]/ul[contains(@class,"listUl")]/li/@logr').extract():
             #gz_2_39755299868183_28191154595392_sortid:1486483205000 @ ses:busitime ^ desc @ pubid:5453707因为58同城的详情页做了爬取限制，所以由自己构造详情页id
             #构造详情页url
               # detail_link='http://dg.58.com/zufang/'+detail_link.split('_')[3]+'x.shtml'
            detail_link = response_url[0]+'/zufang/' + detail_link.split('_')[3] + 'x.shtml'
               #对详情页进行解析cd
            if detail_link:
                inserintota(detail_link,2)
                print '[success] the detail link ' + detail_link + ' is insert into the redis queue'