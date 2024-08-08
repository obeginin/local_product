from django import forms
from .models import Employee

# содаём форму для ввода данных сотрудника
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'birthday']