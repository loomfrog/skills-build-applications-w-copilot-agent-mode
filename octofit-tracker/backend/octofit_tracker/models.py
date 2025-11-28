from djongo import models

class User(models.Model):
	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)
	team = models.CharField(max_length=100)
	def __str__(self):
		return self.username

class Team(models.Model):
	name = models.CharField(max_length=100, unique=True)
	members = models.JSONField(default=list)
	def __str__(self):
		return self.name

class Activity(models.Model):
	user = models.CharField(max_length=100)
	activity = models.CharField(max_length=100)
	distance = models.FloatField()
	def __str__(self):
		return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
	user = models.CharField(max_length=100)
	points = models.IntegerField()
	def __str__(self):
		return f"{self.user}: {self.points}"

class Workout(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	def __str__(self):
		return self.name
