from django.urls import path
from .import views

app_name ='ads'

urlpatterns = [
    path('', views.adshomeview, name='adshomeview'),
]