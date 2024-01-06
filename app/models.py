from django.db import models

# create your models here
class Dept(models.Model):
    Dept_No=models.IntegerField()
    DName=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return 
    
class EMP(models.Model):
    Dept_No=models.ForeignKey(Dept,on_delete=models.CASCADE)
    EID=models.IntegerField()
    Emp_Name=models.CharField(max_length=100,unique=True)
    Job=models.CharField(max_length=100)
    HireDate=models.DateField()
    Sal=models.IntegerField
    Commition=models.IntegerField()
    def __str__(self):
        return 
