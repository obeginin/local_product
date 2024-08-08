from django.db import models

# Создаём модель Employee, которая будет храат анные в БД
class Employee(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    #phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name
