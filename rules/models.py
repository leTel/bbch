from django.db import models

class Rule(models.Model) :
	name = models.CharField(max_length=30)
	description = models.TextField()
	language = models.ForeignKey('Language')
	release_date = models.DateField()
	comments = models.CharField(max_length=100, blank=True, null=True)
	link = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return self.description

class Language(models.Model) :
	name = models.CharField(max_length=4)
	value = models.CharField(max_length=2)

	def __unicode__(self):
		return self.value

class Skill(models.Model) :
	name = models.CharField(max_length=20)
	description = models.TextField()
	s_type = models.ForeignKey('SkillType')

	def __unicode__(self):
		return self.name

class SkillType(models.Model) :
	name = models.CharField(max_length=30)
	letter = models.CharField(max_length=1)

	def __unicode__(self):
		return self.name

class SkillFR(models.Model) :
	name = models.CharField(max_length=20)
	description = models.TextField()
	s_type = models.ForeignKey('SkillTypeFR')

	def __unicode__(self):
		return self.name

class SkillTypeFR(models.Model) :
	name = models.CharField(max_length=30)
	letter = models.CharField(max_length=1)

	def __unicode__(self):
		return self.name