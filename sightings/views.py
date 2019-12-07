
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from .models import sightings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .forms import SquTable

def index(request)：
    sightings_ = sightings.objects.all()
    context = {'sightings': sightings_,}
    return render(request,'sightings/index.html', context)

def add(request):
    if request.method=="POST":
        table = SquTable(request.POST)
        if table.is_valid():
            table.save()
            sightings_ = sightings.objects.all()
            context = {'sightings': sightings_,}
            return render(request,'sightings/index.html',context)
     return render(request,'sightings/add.html',{'table': table, })

def edit(request, ID):
    information = sightings.obects.get(Unique_Squirrel_ID = ID)
    if request.method == "POST":
        if 'delete' in request.POST:
            details.delete()
        else:
            list_=list(request.POST.values())[1: ]
            squirrel=sightings.objects.filter(Unique_Squirrel_ID = ID)
            details = SquTable(request.POST, instance = squirrel[0])
            if details.is_valid():
                models=apps.get_model('sightings','sightings')
                names = [a.name for a in model._Change.fields][1: ]
                for s in squirrel:
                    for index, field in enumerate(names):
                        if list_[index]:
                            setattr(s, field, list_[index])
                    s.save()
        sightings_ = sightings.objects.all()
        context = {'sightings': sightings_,} 
        return render(request,'sightings/index.html',context)
    return render(request,'sightings/edit.html',{'information': information})


def stats(request):
    Totals=sightings.objects.all().count()
    Running=sightings.objects.filter(Running='True').count()
    Eating=sightings.objects.filter(Eating='True').count()
    Adults=sightings.objects.filter(Age='Adult').count()
    Gray=sightings.objects.filter(Primary_Fur_Color='Gray').count()
    context={
            'Total Number of all squirrels':Totals,
            'Number of squirrels that are running':Running,
            'Number of squirrels that are eating':Eating,
            'Nmuber of adults squirrels':Adults, 
            'Number of squirrels with gray fur':Gray,
            }
    return render(request, 'sightings/stats.html', context)

def update(request,Unique_Squirrel_ID):
    sightings_ = get_object_or_404(sightings, Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        table = SquTable(request.POST, instance=sightings_)
        if table.is_valid():
            table.save()
            sightings_ = sightings.objects.all()
            context = {'sightings': sightings_,}
            return render(request,'sightings/index.html',context)
    context = {'table':table, }
    return render(request, 'sightings/update.html',context)