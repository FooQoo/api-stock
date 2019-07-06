from rest_framework import serializers
from .models import Article, Tag, TweetTask
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        read_only_fields = ('updated_at',)
        fields = ('title', 'tags', 'url', 'created_at',)

    def create(self, validated_data):
        tags = validated_data['tags']
        article = Article.objects.create(
            title=validated_data['title'],
            url=validated_data['url'],
            created_at=validated_data['created_at']
        )

        for tag_data in tags:
            tag = Tag.objects.filter(**tag_data).first()
            if tag is None:
                tag = Tag.objects.create(name=tag_data["name"])
            article.tags.add(tag)

        article.save()
        TweetTask.objects.create(article=article)
        return article


class TweetTaskSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = TweetTask
        read_only_fields = ('updated_at', 'created_at')
        fields = ('task_id', 'article', 'status')
