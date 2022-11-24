from django.shortcuts import render
from .models import PhotoExp
from kategories.models import kategories
from django.views.generic import DetailView
from networks.models import Networks
# Create your views here.


class PhototDetail(DetailView):
    model=kategories
    
    
    template_name='./album_page.html'
    context_object_name='category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        cat=self.get_object()
        nw_list=Networks.objects.all()
        photo_list=PhotoExp.objects.filter(category_ph=cat)
        kategories_list=kategories.objects.all()
        context['photo_list']=photo_list
        context ['kategories_list']= kategories_list
        context ['nw_list']=nw_list
        return context

# def album_page(request):

#     photo_list=PhotoExp.objects.all()
    
    
#     dict_obj={'photo_list':photo_list}
#     return render(request, './album_page.html', dict_obj)
    