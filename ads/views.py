from django.http import HttpResponse
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

    def get_queryset(self):
        return models.Ad.objects.order_by('id')


    def head (self, *args, **kwards):
        last_add = self.get_queryset().latest('created_at')
        response = HttpResponse (
                    headers = {'Last created': last_add.created_at.strftime('%a, %d %b %Y %H:%M:%S GMT')}
        )
        return response

def ad_create(request):
    pass