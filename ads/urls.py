from os import name
from django.urls import path, reverse_lazy
from .import views

app_name ='ads'

urlpatterns = [
    path('', views.adshomeview, name='adshomeview'),
    path('all/', views.AdListView.as_view(), name='all'),
    path('ad_create/', views.ad_create, name='ad_create'),
]