from django.shortcuts import render
from slider.models import Slider
from.models import *
from kategories.models import kategories
from telebot.sendmessage import sendTelegram
from networks.models import Networks
# Create your views here.
def first_page(request):
    slider_list=Slider.objects.all()
    kategories_list=kategories.objects.all()
    nw_list=Networks.objects.all()
    


    dict_obj={'slider_list':slider_list, 'kategories_list': kategories_list, 'nw_list':nw_list }
    return render (request, './index.html', dict_obj)

def thanks_page(request):
    if request.POST:
        name=request.POST['name']
        phone=request.POST['phone']
        message=request.POST['message']
        element=order(order_name=name, order_phone=phone, order_message=message)
        element.save()
        link=sendTelegram(tg_name=name, tg_phone=phone, tg_message=message)
        return render (request, './thanks.html', {'name': name,  'phone': phone, 'message':message, 'link':link})
    else: return render (request, './thanks.html')