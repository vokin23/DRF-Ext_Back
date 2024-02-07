from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, WorksViewSet

router = DefaultRouter()
router.register(r'worker', WorkerViewSet)
router.register(r'work', WorksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]