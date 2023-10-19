from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .models import _get_all_articles, _create_article
from .form import create_article_form, login_form

# Create your views here.
def index(request):
    return render(request, "blog/blog.html", context = {
        "articles": _get_all_articles()
    })

@login_required(login_url="/blog/login")
def create_article(request):
    if request.method == "GET":
        return render(request, "blog/create_article.html", context={"form": create_article_form()})
    else:
        _create_article(request)
        return HttpResponse("save Success")
    

###
# auth part
###

def login(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return render(request, 'auth/login.html', context={"form":login_form()})
        return redirect("/blog")
    else:
        user = authenticate(request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        print(user)
        if user != None:
            auth_login(request, user)
            return redirect("/blog")
        else:
            return redirect("/blog/login")


def logout(request):
    if request.user.is_authenticated:
        user_logout(request)
    return redirect("/blog")