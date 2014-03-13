from django.db import models

class Forum(models.Model):
	name = models.CharField(max_length=50)
	area = models.CharField(max_length=2)
	flag = models.CharField(max_length=50)
	languages  = models.CharField(max_length=20)
	link = models.URLField()

	def __unicode__(self):
		return self.name