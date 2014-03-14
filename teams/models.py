from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=30)
	position = models.CharField(max_length=30)
	number = models.IntegerField(unique=True)
	xp = models.IntegerField(default=0)
	value = models.IntegerField(default=50000)
	maximum = models.IntegerField(default=0)
	team = models.ForeignKey('Team')

	def __unicode__(self):
		return ("#"+self.number+" "+self.name+", "+self.position)

class Team(models.Model):
	name = models.CharField(max_length=50)
	size = models.IntegerField(default=0)
	value = models.IntegerField(default=0)
	coach = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class State(models.Model):
	pass

class Race(models.Model):
	pass

class Division(models.Model):
	pass

class League(models.Model):
	pass