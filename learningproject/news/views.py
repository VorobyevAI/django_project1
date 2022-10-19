from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    return render(request, 'news/index.html')




def show_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    list1 = {
        'news': news,
        'category1': category,
    }
    return render(request, template_name='news/category.html', context=list1)



def read_more(request, id_cat):
    new = News.objects.get(id=id_cat)
    list1 = {
        'new': new,
    }
    return render(request, 'news/readmore.html', list1)

def add(request):
    print(request.headers)
    return render(request, 'add.html')


def about(request):
    print(request.headers)
    return render(request, 'about.html')