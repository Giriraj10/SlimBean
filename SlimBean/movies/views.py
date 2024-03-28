from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def home_page(request):
    data = Movie.objects.all()
    return render(request , 'oneview.html',{'data':data})

def detail_view(request , id):
    movie_detail = Movie.objects.get(pk=id)
    return render(request,'movie_detail.html' , {"data" : movie_detail})

def add(request):
    return render(request , 'addmovie.html')

def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/oneview') 
    else:
        form = MovieForm() 
    return render(request, 'addmovie.html', {'form': form})