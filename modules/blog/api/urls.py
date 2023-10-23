from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog' 

urlpatterns = [
    path('', views.index, name='index'),
    path('article', views.create_article),
    path('login', views.login),
    path('logout', views.logout),
]