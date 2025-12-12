from django.contrib import admin
from django.urls import path
from mathserverapp import views
urlpatterns = [path('',views.mileage,name='vehicle')]
