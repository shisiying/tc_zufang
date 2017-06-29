# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import ItemInfo
from django.core.paginator import Paginator
from mongoengine import connect
connect("zufang_fs",host='127.0.0.1')
# Create your views here.
def document(request):
    limit=15
    zufang_info=ItemInfo.objects
    pageinator=Paginator(zufang_info,limit)
    page=request.GET.get('page',1)
    loaded = pageinator.page(page)
    cities=zufang_info.distinct("city")
    citycount=len(cities)
    context={
        'itemInfo':loaded,
        'counts':zufang_info.count,
        'cities':cities,
        'citycount':citycount
    }
    return render(request,'document.html',context)
def binzhuantu():
    ##饼状图
    citys = []
    zufang_info = ItemInfo.objects
    sums = float(zufang_info.count())
    cities = zufang_info.distinct("city")
    for city in cities:
        length = float(len(zufang_info(city=city)))
        ocu = round(float(length / sums * 100))
        item = [city.encode('raw_unicode_escape'), ocu]
        citys.append(item)
    return citys

def chart(request):
    ##饼状图
    citys=binzhuantu()
    # #柱状图
    # zufang_info = ItemInfo.objects
    # res = zufang_info.all()
    # cities = zufang_info.distinct("city")
    # cc = []
    # time = []
    # counts = []
    # for re in res:
    #     if re.pub_time != None:
    #         if re.pub_time > '2017-03-01':
    #             if re.pub_time < '2017-04-01':
    #                 time.append(re.city)
    # for city in cities:
    #     count = time.count(city)
    #     counts.append(count)
    #     item = city.encode('utf8')
    #     cc.append(item)
    context ={
        # 'count': counts,
        # 'citys': cc,
        'cities':citys,
    }
    return render(request,'chart.html',context)
def cloud(request):
    zufang_info = ItemInfo.objects
    res = zufang_info.distinct('community')
    length=len(res)
    context={
        'count':length,
        'wenzi':res
    }
    return render(request, 'test.html',context)

def test(request):
    zufang_info = ItemInfo.objects
    rr=[]
    res = zufang_info.distinct('community')
    i=0
    while i<500:
        item=res[i]
        rr.append(item)
        i=i+1
    length = len(res)
    context = {
        'count': length,
        'wenzi':  rr
    }
    return render(request,'test.html',context)