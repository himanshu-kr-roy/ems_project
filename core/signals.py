from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee

@receiver(post_save,sender=Employee)
def employee_created(sender,instance,created,**kwargs):
    if created:
        print(f'New Employee Added: {instance.user.username} in {instance.department}')