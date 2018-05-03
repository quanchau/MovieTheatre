from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone

from .models import Movie, Showing, Theatre, Cinema

def movies(request):
	movie_list = Movie.objects.order_by('-movie_title')
	context = {
		'movie_list': movie_list,
	}

	return render(request, "reservation/movies.html", context)

def showings(request, movie_id2):

	showing_list = Showing.objects.filter(movie_id = movie_id2)
	context = {
		'showing_list':showing_list,
	}
	return render(request, "reservation/showings.html", context)



def info(request, showing_id):
	showing = get_object_or_404(Showing, id= showing_id)
	movieID = showing.movie_id
	theatreID = showing.theatre_id
	movie = get_object_or_404(Movie, id=movieID)
	theatre = get_object_or_404(Theatre, id=theatreID)
	cinemaID = theatre.cinema_id
	cinema = get_object_or_404(Cinema, id=cinemaID)

	
	context = {
		'showing':showing,
		'movie' :movie,
		'theatre': theatre,
		'cinema': cinema
	}

	return render(request, "reservation/info.html", context)

def insertForm(request):
	return render(request, "reservation/insertForm.html", {})

def insert(request):
	try:
		selected_attribute = request.POST['attribute']
	except(KeyError):
		return render(request, 'reservation/insertForm.html', {
			'error_message': "Choose an attribute!",
		})
	else:
		if (selected_attribute == "movie"):
			m = Movie(movie_title=request.POST['movie-title'], duration=request.POST['duration'],pub_date=timezone.now())
			try: 
				m.save()
			except(KeyError):
				return render(request, 'reservation/insertForm.html', {
			'error_message': "Invalid Input",
				})

		elif (selected_attribute == "cinema"):
			c = Cinema(cinema_name=request.POST['cinema-name'], cinema_addr=request.POST['cinema-address'], cinema_city=request.POST['cinema-city'], cinema_state=request.POST['cinema-state'], cinema_country=request.POST['cinema-country'], cinema_contact = request.POST['cinema-contact'])
			try: 
				c.save()
			except(KeyError):
				return render(request, 'reservation/insertForm.html', {
			'error_message': "Invalid Input",
				})

		elif (selected_attribute == "showing"):
			movieTitle = request.POST['movie-title-showing']
			theatreID = request.POST['theatre-id']
			
			movie = get_object_or_404(Movie, movie_title = movieTitle)
			movieID = movie.id
			date = request.POST['showing-date']
			time = request.POST['showing-time']
			fullDate= date + " " + time
			

			s = Showing(showing_date= fullDate, showing_time = fullDate, theatre_id=request.POST['theatre-id'], movie_id=movieID)
			try: 
				s.save()
			except(KeyError):
				return render(request, 'reservation/insertForm.html', {
			'error_message': "Invalid Input",
				})
		elif (selected_attribute == "theatre"):
			cinemaName = request.POST['theatre-cinema-name']
			cinema = get_object_or_404(Cinema, cinema_name = cinemaName)
			cinemaID = cinema.id
			capacity = request.POST['theatre-capacity']
			t = Theatre(theatre_capacity=capacity, cinema_id = cinemaID)
			try: 
				t.save()
			except(KeyError):
				return render(request, 'reservation/insertForm.html', {
			'error_message': "Invalid Input",
				})


		movie_list = Movie.objects.order_by('-movie_title')
		context = {
			'movie_list': movie_list,
		}
		
		return render(request, 'reservation/movies.html', context)
			

