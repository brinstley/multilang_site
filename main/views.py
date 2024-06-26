from django.shortcuts import render
from .models import Articles

# Create your views here.
def home (request):
    articles = Articles.objects.all()
    #print("-------------{}".format(articles))
    return render(request, 'home.html', {'articles':articles})

def detail(request, titre):
    try:
        article = Articles.objects.get(title = titre)
    except Articles.DoesNotExist:
        raise("Article inexistant")
    
    return render(request, 'detail.html', {'article':article})

def chatbot (request):
    return render(request, 'chatbot.html')
