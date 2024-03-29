from django.db import models

class Carrers(models.Model):
	username = models.CharField(max_length=5000)
	created_datetime = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=50000)
	content = models.CharField(max_length=500000)
	
	class Meta:
		db_table = 'carrers'
		ordering = ['created_datetime']
