from django.conf.urls import url, include
from django.contrib import admin
from stock.urls import router as my_stock_router
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^stock/', include(my_stock_router.urls)),
]
