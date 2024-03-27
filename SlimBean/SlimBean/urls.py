from django.contrib import admin
from django.urls import path
from SlimBean.controller import OneView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',OneView.home),
    path('oneview' , OneView.home_page)
]
