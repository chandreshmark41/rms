from django.db import models


class Student(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    rollnumber = models.CharField(max_length=20)
    branch = models.CharField(max_length=25)
    year = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)


class Admin(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)




