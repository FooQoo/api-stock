from rest_framework import viewsets, response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Article, TweetTask
from .serializers import ArticleSerializer, TweetTaskSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title',)


class TweetTaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = TweetTask.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = TweetTaskSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_fields = ('status', )
    ordering_fields = ('updated_at', )
    ordering = ('updated_at', )
