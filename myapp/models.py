from django.db import models
#from __future__ import unicode_literals

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField()
    mbl=models.IntegerField()
    mail_id = models.EmailField(max_length=30)
    entry_date=models.DateField()
    class Meta:
        db_table = "employee"


