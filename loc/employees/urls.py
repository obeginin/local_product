from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from .views import add_Employee

#настраиваем маршрут для стандартных действий EmployeeViewSet
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('add/', add_Employee, name='add_Employee'),
]
