from os import name
from django.urls import path, reverse_lazy
from .import views

app_name ='ads'

urlpatterns = [
    path('', views.adshomeview, name='adshomeview'),
    path('', views.AdListView.as_view(), name='all'),
    path('', views.ad_create, name='ad_create'),
]