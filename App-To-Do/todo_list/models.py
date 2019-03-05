from django.db import models
from datetime import datetime

# Create your models here.


class List(models.Model):
	item = models.CharField(max_length=200, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	done = models.BooleanField(default=False)
	archived = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	last_edited_on = models.DateTimeField(auto_now=True)

	#Let see if this works.
	def __str__(self):
		return f"{self.id} : {self.item}"