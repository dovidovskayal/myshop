from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]