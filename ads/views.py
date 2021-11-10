from django.shortcuts import render

# Create your views here.

def adshomeview(request):
    return render(request, 'ads/ads_home.html')
    