import re
from django.http import response
from django.shortcuts import get_object_or_404, redirect, render


from .models import Autos
from .models import Make

# Create your views here.


def autohomeview(request):
    return render(request, 'autos/auto_home.html')


def addauto(request):

    if request.method == 'POST':
        obj = Autos()
        obj.nickname = request.POST['nickname']

        make = Make.objects.get(pk = request.POST.get('make'))
        obj.make = make

        obj.milage = request.POST['milage']
        obj.comments = request.POST['comments']
        obj.save()

        return redirect('/autos/listautos')

    else:
        make = Make.objects.all()
        context = {
            'make': make
        }
        return render(request, 'autos/add_auto.html', context)


def autolist(request):

    autolist = Autos.objects.all()

    context = {
        'autolist': autolist
    }
    return render(request, 'autos/auto_list.html', context)


def autoedit(request, id):

    auto_details = get_object_or_404(Autos, pk=id)
    make = Make.objects.all()

    context = {
        'autodetails': auto_details,
        'make' : make,
        'selected_make' : auto_details.make
    }

    if request.method == 'POST' and 'buttonsubmit' in request.POST:

        obj = get_object_or_404(Autos, pk=id)

        obj.nickname = request.POST['nickname']
        obj.make = get_object_or_404(Make, pk=request.POST['make'])
        obj.milage = request.POST['milage']
        obj.comments = request.POST['comments']
        obj.save()

        return redirect('/autos/listautos')

    elif request.method == 'POST' and 'buttondelete' in request.POST:
        return redirect(str(id) + '/deleteauto')

    else:
        return render(request, 'autos/edit_auto.html', context)


def autodelete(request, id):
    Autos.objects.filter(id=id).delete()
    return redirect('/autos/listautos')




def addmake(request):

    if request.method == 'POST':
        obj = Make()
        obj.name_text = request.POST['make']

        obj.save()
        return redirect ('/autos/listmakes')
        #return redirect('auto:makeslist')
    else:
        return render(request, 'autos/add_make.html', {})


def makeslist(request):
    makelist = Make.objects.all()

    context = {
        'makelist': makelist
    }

    return render (request, 'autos/make_list.html',context)


def editmake(request, id):
    make = Make.objects.get(pk=id)
    contex = {
        'make':make
    }

    if request.method == 'POST' and 'buttonupdate' in request.POST:
        obj = get_object_or_404(Make, pk=id)
        obj.name_text = request.POST['make']
        obj.save()

        return redirect('auto:makeslist')

    elif request.method == 'POST' and 'buttondelete' in request.POST:
        return redirect(str(id) + '/deletemake')
    else:
        return render(request, 'autos/edit_make.html', contex)
        



def makedelete(request, id):
    Make.objects.filter(id=id).delete()
    return redirect('auto:makeslist')
