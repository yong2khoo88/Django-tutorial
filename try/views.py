from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from forward.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView, View 

# Create your views here.

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'combine/index.html', context=None)
