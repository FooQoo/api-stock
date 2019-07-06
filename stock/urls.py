from rest_framework import routers
from .views import ArticleViewSet, TweetTaskViewSet


router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)
router.register(r'tweettask', TweetTaskViewSet)
urlpatterns = router.urls
