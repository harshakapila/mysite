from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.

def adshomeview(request):
    return render(request, 'ads/ads_home.html')

class AdListView(CreateView):
    pass

def ad_create(request):
    pass