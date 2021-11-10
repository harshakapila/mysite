from django.urls import path

from .import views

app_name = 'auto'

urlpatterns = [ 
    path('', views.autohomeview, name='autohomeview'),
    path('listautos', views.autolist, name='autolist'),
    path('addauto/', views.addauto, name='addauto'),
    path('<int:id>/editauto', views.autoedit, name='autoedit'),
    path('<int:id>/deleteauto', views.autodelete, name='autodelete'),

    path('listmakes/', views.makeslist, name='makeslist'),
    path('addmake/', views.addmake, name='addmake'),
    path('<int:id>/editmake', views.editmake, name='editmake'),
    path('<int:id>/deletemake', views.makedelete, name='makedelete'),


]