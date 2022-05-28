from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Create your views here.
def home(request):
    context = {
        "articles":  Article.objects.filter(status= 'p'),
    }
    return render(request, "blog/home.html", context)

# یک ویو جدید با آدرس جدید و با گرفتن سلاگ مقاله آن را نمایش می دهد و گت می کند
def detail(request, slug):
    context = {
        "article":  get_object_or_404(Article, slug=slug, status="p"),
    }   
    return render(request, "blog/detail.html", context)


def category(request, slug):    
    context = {
        "category":  get_object_or_404(Category, slug=slug, status=True),
    } 
    return render(request, "blog/category.html", context)