from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
from account.models import shop
from .models import announce
import datetime
# Create your views here.
#search-
#announcment-location

def search(request):
    keyword = request.GET['q']
    lat = int(request.GET['lat'])
    longt = int(request.GET['longt'])
    result = shop.objects.filter(
        shop_name__contains=keyword,
        latitude__range=(lat-10,lat+10),
        longtitude__range=(longt-10,longt+10)
    )
    result=result.values(
        'shop_name',
        'own_name',
        'address',
        'latitude',
        'longtitude',
        'sunday',
        'curr_start',
        'curr_end',
        'open',
        )
    result=[x for x in result]
    processOpen(result)
    return JsonResponse(result,safe=False)

def announcment(request):
    lat = int(request.GET['lat'])
    longt = int(request.GET['longt'])
    result = announce.objects.filter(
        shop__latitude__range=(lat-10,lat+10),
        shop__longtitude__range=(longt-10,longt+10)
    )
    result=result.values(
        'description',
        'shop__shop_name',
    )
    result=[x for x in result]
    return JsonResponse(result,safe=False)

@login_required
def addAnnounce(request):
    desc = request.GET['desc']
    shop = request.user.shop
    ann = announce(shop=shop,description=desc)
    ann.save()
    return HttpResponse('1')

def processOpen(res):
    curr = datetime.datetime.now().time()
    for i in res:
        if(i.curr_start<=curr<=i.curr_end):
            i.open=True