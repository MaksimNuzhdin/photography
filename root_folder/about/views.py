from django.shortcuts import render
from .models import About
from kategories.models import kategories
from networks.models import Networks
# Create your views here.
def about_page(request):
    ab=About.objects.get(pk=1)
    kategories_list=kategories.objects.all()
    nw_list=Networks.objects.all()
    return render (request, './about.html', {'ab':ab, 'kategories_list': kategories_list, 'nw_list':nw_list})