from django.shortcuts import render
from .models import Articles

# Cette vue lis les articles dans la base de donnees et les retournes
def home (request):
    articles = Articles.objects.all()
    #print("-------------{}".format(articles))
    return render(request, 'home.html', {'articles':articles})

# Cette vue lis les details d'un article dans la base de donnees et les retouners
def detail(request, titre):
    try:
        article = Articles.objects.get(title = titre)
    except Articles.DoesNotExist:
        raise("Article inexistant")
    
    return render(request, 'detail.html', {'article':article})
# Cette vue retourne la page du chatbot
 def chatbot (request):
    return render(request, 'chatbot.html')
