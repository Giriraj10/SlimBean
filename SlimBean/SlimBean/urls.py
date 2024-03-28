from django.contrib import admin
from django.urls import path
from movies import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('oneview' , views.home_page),
    path('movie/<int:id>' , views.detail_view), 
    path('movie/add', views.add_movie, name='add_movie'),
    path('api/movies/', views.MovieListCreateAPIView.as_view(), name='movie-list-create'),
]

