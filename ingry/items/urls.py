from django.urls import path, include
from .views import ItemsViewSet, MyView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', ItemsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
