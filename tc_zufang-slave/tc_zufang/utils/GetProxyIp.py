# -*- coding: utf-8 -*-
import random
import requests
def GetIps():
    li=[]
    global count
    url ='http://139.199.182.250:8000/?types=0&count=300'
    ips=requests.get(url)
    for ip in eval(ips.content):
        li.append(ip[0]+':'+ip[1])
    return li

GetIps()
