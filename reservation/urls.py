from django.urls import path

from . import views

app_name = 'reservation'
urlpatterns = [
	path('', views.movies, name='movies'),
	path('<int:movie_id2>/showings/', views.showings, name='showings'),
	path('<int:showing_id>/info', views.info, name='info'),
	path('insertForm/', views.insertForm, name='insertForm'),
	path('insert/', views.insert, name='insert'),
]
