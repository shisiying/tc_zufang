# -*- coding: utf-8 -*-
import random
import redis
import requests
# def GetIps():
#     li=[]
#     url ='http://127.0.0.1:8000/?types=0&count=100'
#     ips=requests.get(url)
#     for ip in eval(ips.content):
#         li.append(ip[0]+':'+ip[1])
#     try:
#         num = random.randint(0, len(li))
#         ress = 'http://' + li[num]
#     except:
#         print 'have not enough ip!'
#     return str(ress)
def GetIps():
    li=[]
    global count
    url ='http://127.0.0.1:8000/?types=0&count=300'
    ips=requests.get(url)
    for ip in eval(ips.content):
        li.append(ip[0]+':'+ip[1])
    return li
GetIps()