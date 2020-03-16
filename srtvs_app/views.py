from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from datetime import datetime, time, timezone
from .models import Show

def home(request): 
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'home.html', context)

def add_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/home')
    else:
        show = Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        messages.success(request, "Show successfully updated!")
    return redirect(f'/shows/{show.id}')

def TvShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'view_shows.html', context)

def AllShows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def EditShow(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }
    return render(request, 'edit_shows.html', context)
    

def UpdateShow(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
    return redirect(f'/shows/{id}')

def DeleteShow(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')

def index(request):
    return redirect('/shows')

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/{show.id}/edit')
    else:
        shows = Show.objects.get(id = id)
        shows.title = request.POST['title']
        shows.network = request.POST['network']
        shows.description = request.POST['description']
        shows.save()
        messages.success(request, "Show successfully updated!")
        return redirect('view_shows.html')
