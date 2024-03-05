from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, DeviceLogViewSet, DeviceViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet),
router.register(r'devices', DeviceViewSet)
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
