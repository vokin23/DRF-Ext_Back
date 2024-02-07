from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkerViewSet, WorksViewSet

router = DefaultRouter()
router.register(r'worker/get_data', WorkerViewSet)
router.register(r'work/get_data', WorksViewSet)

urlpatterns = [
    path('', include(router.urls))
]