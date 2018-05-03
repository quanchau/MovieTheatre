

-- ----------------------
-- Create Cinema table
-- ----------------------
CREATE TABLE Cinema
(
	cinema_id		char(20) NOT NULL,
	cinema_name		char(20) NULL,
	cinema_address char(50)  NULL ,
	cinema_city    char(50)  NULL ,
	cinema_state   char(5)   NULL ,
	cinema_zip     char(10)  NULL ,
	cinema_country char(50)  NULL ,
	cinema_contact char(50)  NULL
);

-- -----------------------
-- Create Theater table
-- ----------------------
create table Theater
(
	theater_id 	char(20) not null,
	theater_capacity	char(20) null,
    cinema_id char(20) not null
);

-- -----------------------
-- Create Showing table
-- -----------------------
create table Showing
(
	showing_id			char(20) not null,
	showing_time		char(20) not null,
	showing_date		datetime not null,
	theater_id			char(20)	not null,
    movie_id 			char(20) not null
);

-- ------------------------
-- Create Movie table
-- -----------------------
create table Movie
(
	movie_id		char(20) not null,
	movie_title		char(50) null,
	movie_released_date		datetime null,
    movie_duration	int null
);


-- -------------------
-- Define primary keys
-- -------------------
alter table Cinema add primary key (cinema_id);
alter table Theater add primary key (theater_id);
alter table Movie add primary key (movie_id);
alter table Showing add primary key (showing_time, showing_date, showing_id);

-- -------------------
-- Define foreign keys
-- -------------------
ALTER TABLE Theater ADD CONSTRAINT FK_Theater_Cinema FOREIGN KEY (cinema_id) REFERENCES Cinema (cinema_id);
ALTER TABLE Showing ADD CONSTRAINT FK_Showing_Movie FOREIGN KEY (movie_id) REFERENCES Movie (movie_id);
ALTER TABLE Showing ADD CONSTRAINT FK_Showing_Theater FOREIGN KEY (theater_id) REFERENCES Theater (theater_id);

