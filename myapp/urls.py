
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('contact/', views.contact, name='contact'),

]
