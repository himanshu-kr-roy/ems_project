from rest_framework import viewsets,permissions
from .models import Department,Employee,Payroll
from .serializers import DepartmentSerializer,EmployeeSerializer,PayrollSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all().select_related('employee')
    serializer_class = PayrollSerializer
    permission_classes = [permissions.IsAuthenticated]
