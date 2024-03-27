from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from .models import Movie

def home(request):
    return HttpResponse("Home!")

def home_page(request):
    data = Movie.objects.all()
    return render(request , 'oneview.html',{'data':data})

def detail_view(request , id):
    movie_detail = Movie.objects.get(pk=id)
    return render(request,'movie_detail.html' , {"data" : movie_detail})

def add(request):
    return render(request , 'addmovie.html')

def savemovie(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    id = request.POST.get('id')
    description = request.POST.get('description')
    if title and year and id:
        movie = Movie(id= id ,title = title,year = year)
        if description:
            movie.description = description
        movie.save()
        return HttpResponseRedirect('/oneview')
    
    return HttpResponse("Error Saving")
