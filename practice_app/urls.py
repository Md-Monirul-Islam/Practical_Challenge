from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, DeviceViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet),
router.register(r'devices', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
