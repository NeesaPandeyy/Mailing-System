from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('customer','Customer'),
    )
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='customer')

    def is_admin(self):
        return self.role == 'admin'
    
    def is_customer(self):
        return self.role == 'customer'

