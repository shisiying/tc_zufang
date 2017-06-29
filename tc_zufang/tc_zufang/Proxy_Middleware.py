# -*- coding: utf-8 -*-
# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64
import random
from tc_zufang.utils.GetProxyIp import GetIps

# Start your middleware class
class ProxyMiddleware():
    global count
    count=1
    global ips
    ips=[]
    # overwrite process request
    # def process_request(self, request, spider):
    #     # Set the location of the proxy
    #     global count
    #     if count%4==0:
    #         print '####'
    #         ip=GetIps()
    #         request.meta['proxy'] = ip
    #         print request.meta
    #         print 'get the proxyIp'
    #     count+=1
    #     print 'the ip count is %d'%(count)

    def process_request(self, request, spider):
        # Set the location of the proxy
        global count
        global ips
        if count == 1:
            # print 'the first#############'
            ips = GetIps()
        elif count % 100 == 0:
            # print '#####'
            # print count
            ips = []
            ips = GetIps()
        else:
            pass
        try:
            # print count
            num = random.randint(0, len(ips))
            ress = 'http://' + ips[num]
        except:
            # print 'try to get another ip!'
            # return request.replace(dont_filter=True)
            #使用本机ip进行爬取
            pass
        else:
            request.meta['proxy'] = str(ress)
            count += 1