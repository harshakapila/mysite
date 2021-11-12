from os import name
from django.urls import path, reverse_lazy
from .import views

app_name ='ads'

urlpatterns = [
    path('', views.adshomeview, name='adshomeview'),
    path('all/', views.AdListView.as_view(), name='all'),
    path('ad_create/', views.ad_create, name='ad_create'),
    path('<int:id>/ad_delete', views.ad_delete, name='ad_delete'),
    path('<int:id>/ad_edit', views.ad_edit, name='ad_edit'),
]
