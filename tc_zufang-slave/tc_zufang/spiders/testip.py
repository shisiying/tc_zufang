# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from scrapy.selector import Selector
class testSpider(RedisSpider):
    name = 'testip'
    redis_key = 'testip'
    def parse(self,response):
        response_selector = Selector(response)
        code=response_selector.xpath(r'//div[contains(@class,"well")]/p[1]/code/text()')
        print code

