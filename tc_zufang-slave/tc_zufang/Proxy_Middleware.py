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
    def process_request(self, request, spider):
        # Set the location of the proxy
        global count
        global ips
        if count==1:
            ips= GetIps()
        elif count%100==0:
            ips=[]
            ips=GetIps()
        else:
            pass
        try:
            num = random.randint(0, len(ips))
            ress = 'http://' + ips[num]
        except:
            # print 'try to get another ip!'
            # return request.replace(dont_filter=True)
            # 使用本机ip进行爬取
            pass
        else:
            request.meta['proxy'] = str(ress)
            count += 1