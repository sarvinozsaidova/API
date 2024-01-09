from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'datas', DataViewSet)
urlpatterns = [
    # path('', views.getData),
    path('api/', include(router.urls)),
    # path('post/', views.postData),
]