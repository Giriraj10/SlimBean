from django.contrib import admin
from django.urls import path
from movies import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home),
    path('oneview' , views.home_page),
    path('movie/<int:id>' , views.detail_view),
    path('movie/add',views.add),
    path('movie/savemovie',views.savemovie)
]
