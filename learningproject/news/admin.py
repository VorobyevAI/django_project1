from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'created_at', 'content', 'is_publish' )
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('category', )
    list_editable = ('is_publish', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', )



admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)



