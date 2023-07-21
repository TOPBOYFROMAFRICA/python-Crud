from django.db import models

# create models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
