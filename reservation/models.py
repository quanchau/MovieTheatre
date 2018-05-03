from django.db import models
from django.utils import timezone


# Create your models here.

class Movie(models.Model):
	movie_title = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	duration = models.IntegerField(default = 0)

	def __str__(self):
		return self.movie_title

class Cinema(models.Model):
	cinema_name = models.CharField(max_length=200)
	cinema_addr = models.CharField(max_length=200)
	cinema_contact = models.CharField(max_length=20)
	cinema_city = models.CharField(max_length=200)
	cinema_state = models.CharField(max_length=2)
	cinema_country = models.CharField(max_length=200)


class Theatre(models.Model):
	theatre_capacity = models.IntegerField(default = 0)
	cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE,null=True)

class Showing(models.Model):
	showing_time = models.DateTimeField('show time')
	showing_date = models.DateTimeField('show date')
	theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, default = 1)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default= 1)
	







	
