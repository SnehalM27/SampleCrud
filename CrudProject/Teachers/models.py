from django.db import models


class TeachersModel(models.Model):
    tid = models.IntegerField()
    fnm = models.CharField(max_length=30)
    lnm = models.CharField(max_length=30)
    sal = models.FloatField()
