-- SQL Code to create database for users
CREATE DATABASE GOL_users;
USE GOL_users;

CREATE TABLE the_users (
    UserID int,
    FirstName varchar(65),
	LastName varchar(65),
    Email varchar(65),
    DOB DATE,
    City varchar(65),
    Username varchar(65),
	UserPassword varchar(65)
);



CREATE TABLE searched_words (
    word varchar(50) NOT NULL,
    definition_ varchar(6000) NOT NULL
);

INSERT INTO the_users (UserID, FirstName, LastName, Email, DOB, City, Username, UserPassword)
VALUES (1, 'Jake', 'Callow', 'jcal@email.com', str_to_date('05-12-1992', '%d-%m-%Y'), 'London', 'cobrien1', 'cat123'),
(2, 'Fred', 'Smith', 'fsmith@email.com', 1995-02-19, 'Bristol', 'freddy95', 'bristol11'),
(3, 'Hayley', 'Bieber', 'hayley99@email.com', 1997-09-01, 'Cambridge', 'hbieber1997', 'ilovejustin1'),
(4, 'Luciano', 'Sovino', 'lucosovino89@email.com', 1989-10-29, 'Cardiff', 'lucosov89', 'helloworld0');

