from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('activities', views.activities, name = 'activities'),
    path('team', views.team, name = 'team'),
    path('contact', views.contact, name = 'contact'),
]