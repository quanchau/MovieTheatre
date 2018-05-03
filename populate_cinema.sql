insert into reservation_cinema (cinema_name, cinema_addr, cinema_city, cinema_state, cinema_country, cinema_contact)
values('Carlisle Commons', '250 Noble Blvd', 'Carlisle', 'PA', 'USA', '717-240-0696');
insert into reservation_cinema (cinema_name, cinema_addr, cinema_city, cinema_state, cinema_country, cinema_contact)
values('Carlisle Theatre', '40 W High St', 'Carlisle', 'PA', 'USA', '717-240-0970');
insert into reservation_cinema (cinema_name, cinema_addr, cinema_city, cinema_state, cinema_country, cinema_contact)
values('AMC', '4950 Carlisle Pike', 'Mechanicsburg', 'PA', 'USA', '717-737-4133');

insert into reservation_theatre (theatre_capacity, cinema_id)
values('48', '1');
insert into reservation_theatre (theatre_capacity, cinema_id)
values('45', '1');
insert into reservation_theatre (theatre_capacity, cinema_id)
values('54', '2');
insert into reservation_theatre (theatre_capacity, cinema_id)
values( '55', '2');
insert into reservation_theatre (theatre_capacity, cinema_id)
values('60', '3');
insert into reservation_theatre (theatre_capacity, cinema_id)
values( '65', '3');


insert into reservation_movie (movie_title, pub_date, duration)
values('Toy Story', '1995-10-30', 81);
insert into reservation_movie (movie_title, pub_date, duration)
values('Jumanji', '1995-12-15', 104);
insert into reservation_movie (movie_title, pub_date, duration)
values('Se7en', '1995-09-22', 127);
insert into reservation_movie ( movie_title, pub_date, duration)
values('Star Wars', '1977-05-25', 121);
insert into reservation_movie (movie_title, pub_date, duration)
values('Blade Runner', '1982-06-25', 117);


insert into reservation_showing (showing_time, showing_date, theatre_id, movie_id)
values ('2018-04-28 17:50:00', '2018-04-28 17:50:00', '1', '1');
insert into reservation_showing (showing_time, showing_date, theatre_id, movie_id)
values ('2018-04-28 13:30:00', '2018-04-28 13:30:00', '2', '2');
insert into reservation_showing (showing_time, showing_date, theatre_id, movie_id)
values ('2018-04-28 19:45:00', '2018-04-28 19:45:00', '3', '3');
insert into reservation_showing (showing_time, showing_date, theatre_id, movie_id)
values ('2018-04-28 12:30:00', '2018-04-28 12:30:00', '4', '4');
insert into reservation_showing (showing_time, showing_date, theatre_id, movie_id)
values ('2018-04-28 14:20:00', '2018-04-28 14:20:00', '5', '5');
