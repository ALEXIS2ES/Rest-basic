
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'person', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
