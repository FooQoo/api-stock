from rest_framework import serializers
from .models import Article, Tag, TweetTask


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)

    def create(self, validated_data):
        tag = Tag.objects.filter(name=validated_data['name']).first()
        if tag is None:
            tag = Tag.objects.create(name=validated_data['name'])
        return tag


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
            tag = Tag.objects.filter(name=tag_data['name']).first()
            if tag is not None:
                article.tags.add(tag)

        article.save()
        return article


class TweetTaskSerializer(serializers.ModelSerializer):
    article = ArticleSerializer()

    class Meta:
        model = TweetTask
        read_only_fields = ('updated_at', 'created_at')
        fields = ('task_id', 'article', 'status')

    def create(self, validated_data):
        article = Article.objects.get(article_id=validated_data['article_id'])
        task = TweetTask.objects.create(article=article)
        return task
