from django.shortcuts import render

# Create your views here.
from .models import Colum, Article
from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
    columns = Colum.objects.all()
    return render(request,'index.html',{'columns':columns})

def column_detail(request, column_slug):
    column = Colum.objects.get(slug=column_slug)

    article_set=column.article_set.all()
    # for article in article_set:
    #    print(article.get_absolute_url())
    return render(request, 'news/column.html', {'column': column,'article_set':article_set})


def article_detail(request,pk,article_slug):
    #articl2 = Article.objects.get(slug=article_slug)
   # article = Article.objects.filter(slug=article_slug)[0]


    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return  redirect(article,permanent=True)
    return render(request, 'news/article.html', {'article': article})
