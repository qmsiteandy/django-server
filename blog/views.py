from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import _get_all_articles, _create_article
from .form import create_article_form

# Create your views here.
def index(request):
    return render(request, "blog.html", context = {
        "articles": _get_all_articles()
    })

def create_article(request):
    if request.method == "GET":
        return render(request, "create_article.html", context={"form": create_article_form()})
    else:
        _create_article(request)
        return HttpResponse("save Success")