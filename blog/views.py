from django.shortcuts import render
from django.http import HttpResponse
from .models import _get_all_articles

# Create your views here.
def index(request):
    return render(request, "blog.html", context = {
        "articles": _get_all_articles()
    })

def article(request):
    if request.method == "GET":
        return render(request, "create_articles.html")
    else:
        return 