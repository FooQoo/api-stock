from django.contrib import admin
from .models import Article, Tag, TweetTask


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(TweetTask)
class TweetTaskAdmin(admin.ModelAdmin):
    pass
