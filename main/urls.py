from django.contrib import admin
from django.urls import path
from .views import home, detail, chatbot

# Definition de nos Urls 
urlpatterns = [
    path('', home, name= 'home'),
    path('chatbot/', chatbot, name='chatbot'),
    path('<slug:titre>/', detail, name= "detail"),
    
]

