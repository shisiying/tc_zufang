# -*- coding: utf-8 -*-
from scrapy.http import request
from scrapy.downloadermiddlewares.downloadtimeout import DownloadTimeoutMiddleware
class Timeout_Middleware(DownloadTimeoutMiddleware):
    # def process_response(self, request, response, spider):
    #     http_code = response.status
    #     print "####timeout"
    #     print http_code
    #     print '######timeout'
    #     # return request
    def process_exception(self,request, exception, spider):
        # print "######the downloader return exception!"
        print exception
        return request.replace(dont_filter=True)