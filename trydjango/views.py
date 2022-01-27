from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
import random

def home_view(request):
    name = "Alasdair" # change to logged in userID if logged in
    random_id = random.randint(1,3)
    article_obj = Article.objects.get(id=random_id)
    article_list = Article.objects.all()
        
    context = {
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
        "article_list": article_list,
    }
    
    HTML_STRING = render_to_string('home-view.html', context=context)
        
    return HttpResponse(HTML_STRING)