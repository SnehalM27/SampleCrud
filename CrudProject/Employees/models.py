from django.db import models

class EmployeeModel(models.Model):
    eid = models.IntegerField()
    nm = models.CharField(max_length=30)
    sal = models.FloatField()
    
