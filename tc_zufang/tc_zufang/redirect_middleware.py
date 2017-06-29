#!/usr/bin/python
#-*-coding:utf-8-*-
import urlparse

from scrapy.exceptions import IgnoreRequest
from scrapy.exceptions import CloseSpider
from scrapy.http import Request

from tc_zufang.utils.message import sendMessage_warning

class Redirect_Middleware():
    '''这里重点讲解一下关于处理下载器刚下载下来的response。在spidermiddleware中，我禁掉了httperror中间件，其中的原因是，我禁止了scrapy自带下载中间件中重定向，重试以及metarefeash中间件。原因是这非常的影响爬虫的性能，只会增加爬虫的消耗，而不会带来任何好处。为什么这么说呢？

每一次的重定向，都有可能增加dns解析，tcp/ip链接，然后才是发送http请求。我们为什么要浪费这么多的时间，没任何理由。所以我的做法是，接受任何响应，然后在下载中间件中处理这个响应，过滤出200状态码的相应交给engine.对于那么重定向的(301, 302,meta-refreash等)，我提取出响应头部中的’location’等，然后重新生成一个request对象，交给调度器重新调度。对于404响应，直接抛弃。对于500+响应，把初始request对象重新交给调度器。这样，既不会影响爬虫的正常抓取，也不会落下需要再次抓取的request对象。'''

    global count
    count = 1
    def process_response(self, request, response, spider):
        # 处理下载完成的response
        # 排除状态码不是304的所有以3为开头的响应

        http_code = response.status
        if http_code // 100 == 2:
            return response

        if http_code // 100 == 3 and http_code != 304:
            # 获取重定向的url
            # url = response.headers['location']
            # domain = urlparse.urlparse(url).netloc
            # 判断重定向的url的domain是否在allowed_domains中
            # if domain in spider.allowed_domains:
            #     return Request(url=url, meta=request.meta)
            # else:
            global count
            if count == 1:
                sendMessage_warning()
            print '302'
            count += 1
            #把request返回到下载器
            return request.replace(dont_filter=True)
        if http_code // 100 == 4:
            # 需要注意403不是响应错误，是无权访问
            raise IgnoreRequest(u'404')

        if http_code // 100 == 5:
            return request.replace(dont_filter=True)
