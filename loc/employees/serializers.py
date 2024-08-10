from rest_framework import serializers
from .models import Employee

# с помощю сериализатора преобразуем данные модели в JSON
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'birthday','phone_number']
