from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    # подключаем админку
    path('admin/', admin.site.urls),
    # подключаем файл urls.py из приложения employees
    path('api/', include('employees.urls')),
]
