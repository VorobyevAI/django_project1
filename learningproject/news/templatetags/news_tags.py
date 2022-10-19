from django import template
from news.models import Category, News

register = template.Library()



@register.simple_tag(name='categorys')
def get_category():
    return Category.objects.all()


@register.simple_tag(name='news')
def get_news():
    return News.objects.all()