from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render, redirect
from .forms import EmployeeForm

# ViewSet управляет операциями (создание, чтение, обновление, удаление) для модели
# т.е. предоставляет стандартные действия для работы с моделью через API,
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# отдеьная форма
def add_Employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Замените на вашу страницу или URL
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})


