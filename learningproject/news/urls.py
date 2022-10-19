from django.contrib import admin
from django.urls import path
from news.views import *
urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>', show_category, name='category'),
    path('readmore/<int:id_cat>', read_more, name='readmore'),
    path('add/', add, name='add'),
    path('about/', about, name='about')

]

