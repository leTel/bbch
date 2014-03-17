from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=30)
	position = models.CharField(max_length=30)
	number = models.IntegerField(unique=True)
	xp = models.IntegerField(default=0)
	value = models.IntegerField(default=50)
	maximum = models.IntegerField(default=0)
	team = models.ForeignKey('Team')
	ma = models.IntegerField(default=6)
	st = models.IntegerField(default=3)
	ag = models.IntegerField(default=3)
	av = models.IntegerField(default=7)


	def __unicode__(self):
		return ("#"+self.number+" "+self.name+", "+self.position)

class Team(models.Model):
	name = models.CharField(max_length=50)
	size = models.IntegerField(default=0)
	value = models.IntegerField(default=0)
	coach = models.CharField(max_length=30)
	reroll = models.IntegerField(default=0)
	reroll_value = models.IntegerField(default=50)
	treasury = models.IntegerField(default=1000)
	apo = models.BooleanField(default=False)
	assistant = models.IntegerField(default=0)
	pompom = models.IntegerField(default=0)
	pop = models.IntegerField(default=0)

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