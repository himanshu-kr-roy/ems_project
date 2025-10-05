from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name='employees')
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.user.username
    
class Payroll(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='payrolls')
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee.user.username} - {self.month}'
