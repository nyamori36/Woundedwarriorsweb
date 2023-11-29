from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
DepartmentList=(
    ('Human Resource','Human Resource'),
    ('Sales','Sales'),
    ('Marketing','Marketing')
)
Roles=(
    ('Manager','Manager'),
    ('Cashier','Cashier'),
    ('Admin','Admin'),

)

Resident=(
    ('Arusha','Arusha'),
    ('Nairobi','Nairobi'),
    ('Kisumu','Kisumu'),
)

State=(
    ('Kenya', 'Kenya'),
    ('Tanzania', 'Tanzania'),
    ('Uganda', 'Uganda'),
)

class Department (models.Model):
    Department=models.CharField(max_length=200,primary_key=True,Choices=Department)

class Employee (models.Model):
    Fullname=models.CharField(max_length=200)
    Role=models.CharField(max_length=200,choices=Role)
    Email=models.CharField(max_length=200,primary_key=True)
    Department=models.ForeignKey(Department,on_delete=models.CASCADE())

class Announcement (models.Model):
    Logo=models.IntegerField_to="Announcements/")
    Heading=models.CharField(max_length=200)
    Document=models.FileField(upload_to=Document/")
    DateRegistered=models.DateTimeField(auto_now_add=True)

class Customer (models.Model):
    Fullname=models.CharField(max_length=200)
    Email=models.CharField(max_length=200,primary_key=True)
    Resident=models.CharField(max_length=20,choices=Resident)
    NationalID=models.CharField(max_length=200)
    State=models.CharField(max_length=200,choices=state)
    License=models.FileField(upload_to="License/")
    DateRegistered = models.DateTimeField(auto_now_add=True)
    About=RichTextField(blank=True,null=True



class Compensation (models.Model):

class MonthlyInstallments (models.Model):



