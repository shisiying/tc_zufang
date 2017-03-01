from django.shortcuts import render
from models import ItemInfo
from django.core.paginator import Paginator
from mongoengine import connect
connect("zufang_fs",host='127.0.0.1',port=27017)
# Create your views here.
def test(request):
    return render(request,'base.html')
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
def chart(request):
    return render(request,'chart.html')
