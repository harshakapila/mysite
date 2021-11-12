import django
from django.contrib.messages.api import error
from django.http import HttpResponse, request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from ads import models
from ads.forms import AdForm
from django.contrib import messages
from django.contrib.auth import get_user_model



from ads.models import Ad

# Create your views here.

def adshomeview(request):
    ads= models.Ad.objects.order_by('id')
    context = {
          'ads':ads,
      }

    return render(request, 'ads/ads_home.html', context)


class AdListView(ListView):
    ad = Ad
    template_name = 'ads/ad_list.html'
    
    def get(self, request, *args, **kwargs):
      ads= models.Ad.objects.order_by('id')
      
      context = {
          'ads':ads,
      }
      return render(request, self.template_name, context)




def ad_create(request):

    template ="ads/ad_create.html"

    if request.method == 'POST':
        ad_form = AdForm(request.POST, request.FILES)
        if ad_form.is_valid():
            ad_form.save()
            messages.success(request, ("Your Ad was created sucessfully"))
        else:
            messages.error(request, "Error saving form")
        
        return redirect("ads:adshomeview")
    
    ad_form = AdForm()
    ads = Ad.objects.all()
    context={
        'ad_form':ad_form,
        'ads':ads,
        }
    return render(request, template, context )
        

def ad_delete(request, id):
    Ad.objects.filter(id=id).delete()

    return redirect("ads:adshomeview")

def ad_edit(request, id):
    addetail = Ad.objects.get(id=id)

    User = get_user_model()
    users = User.objects.all()
    
   
    context = {
        'addetails':addetail,
        'owners': users,
    }

    if request.method == 'POST' and 'buttonsubmit' in request.POST: 
        obj = get_object_or_404(Ad, pk=id)
        
        obj.title = request.POST.get('title')
        obj.price = request.POST.get('price')
        obj.text = request.POST.get('text')
        ownername = request.POST.get('owner')
        print(request.POST.get('owner'))

        owner = get_object_or_404(User, username = ownername)

        obj.owner = owner
        obj.save()

        return redirect('/ads/all')
    else:
        return render (request, 'ads/ad_edit.html', context)
    