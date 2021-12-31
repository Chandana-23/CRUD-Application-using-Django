from django.db import models
from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
