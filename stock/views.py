from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Article, TweetTask
from .serializers import ArticleSerializer, TweetTaskSerializer, TagSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title',)

    def perform_create(self, serializer):

        for tag in self.request.data['tags']:
            tag_serializer = TagSerializer(data=tag)
            tag_serializer.is_valid()
            tag_serializer.save()

        article = serializer.save()

        task_serializer = TweetTaskSerializer()
        task_serializer.create({'article_id': article.article_id})

    def perform_destroy(self, instance):
        article_id = instance.article_id
        task = TweetTask.objects.get(article_id=article_id)
        task.delete()
        instance.delete()


class TweetTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TweetTask.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = TweetTaskSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('status', )
    ordering_fields = ('updated_at', )
    ordering = ('updated_at', )
