from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50,)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField(auto_now_add=True)

def _get_all_articles():
    return Articles.objects.all()

def _create_article(request):
    Articles.objects.create(title=request.POST.get("title"), 
                            content=request.POST.get("content"),
                            image=request.FILES.get('image', 'None'))
    return