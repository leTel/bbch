from django.db import models

class New(models.Model) :
	title = models.CharField(max_length=40)
	content = models.TextField()
	categories = models.ForeignKey('NewCategory')
	language = models.ForeignKey('Language')
	published_date = models.DateField(blank=True, null=True)

	def __unicode__(self):
		return self.title

class NewCategory(models.Model) :
	name = models.CharField(max_length=20)
	category = models.CharField(max_length=3)
	description = models.CharField(max_length=50, blank=True, null=True)

	def __unicode__(self):
		return self.category

class Language(models.Model) :
	name = models.CharField(max_length=4)
	value = models.CharField(max_length=2)

	def __unicode__(self):
		return self.value