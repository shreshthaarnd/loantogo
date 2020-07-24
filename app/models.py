from django.db import models

# Create your models here.
class Data(models.Model):
	Name=models.CharField(max_length=100)
	Address=models.CharField(max_length=200)
	Phone=models.CharField(max_length=15)
	Identity=models.CharField(max_length=50)
	Reason=models.CharField(max_length=100)
	class Meta:
		db_table="Data"