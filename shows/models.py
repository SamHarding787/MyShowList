from django.db import models

class Show(models.Model):
	title = models.CharField(max_length=200)
	genre = models.CharField(max_length=100, blank=True)
	rating = models.IntegerField(null=True, blank=True)
	date_watched = models.DateField(null=True, blank=True)
	notes = models.TextField(blank=True)

	def __str__(self):
		return self.title
