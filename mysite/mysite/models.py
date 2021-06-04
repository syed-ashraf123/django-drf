from django.db import models
class EmployeeModel(models.Model):
    Empid=models.IntegerField(primary_key=True)
    Empname=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Salary=models.IntegerField()
    # def __str__(self):
    #     return self.name or ''