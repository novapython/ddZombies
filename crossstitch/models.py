from django.db import models

# Create your models here.

class Patterns(models.Model):

	name = models.CharField(max_length=64)
	count = models.IntegerField()
	grid = models.CharField(max_length=16)
	image = models.CharField(max_length=128)


class Zombies(models.Model):

	name = models.CharField(max_length=64)
	rotdegree = models.IntegerField()
	favorite = models.ForeignKey(Patterns)