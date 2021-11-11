from django.http import HttpResponse, request
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ads import models

from ads.models import Ad

# Create your views here.

def adshomeview(request):
    return render(request, 'ads/ads_home.html')

class AdListView(ListView):
    ad = Ad
    template_name = 'ads/ad_list.html'
    
    def get_queryset(self):
      ads= models.Ad.objects.order_by('id')
      
      context = {
          'ad':'ads',
      }
      return context




def ad_create(request):
    return render(request, 'ads/ad_create.html')