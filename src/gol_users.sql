-- SQL Code to create database for users
-- RUN THIS CODE SCRIPT IN MYSQL WORKBENCH

CREATE DATABASE GOL_users;
USE GOL_users;

-- CREATING THE DB Tables:

CREATE TABLE the_users (
    UserID int(10) AUTO_INCREMENT NOT NULL,
    FirstName varchar(65),
	LastName varchar(65),
    Email varchar(65) UNIQUE,
    DOB DATE,
    City varchar(65),
    Username varchar(65) UNIQUE,
	UserPassword varchar(65),
	LastLogin DATE,
	UserStreak Int,

CONSTRAINT
    pk_user_id PRIMARY KEY (UserID));


    CREATE TABLE searched_words (
	SearchedWordID int(100) AUTO_INCREMENT,
	UserID int(10),
    word varchar(50) NOT NULL,
    definition_ varchar(6000) NOT NULL,
    PRIMARY KEY (SearchedWordID),
    FOREIGN KEY (UserID) REFERENCES the_users (UserID)
    );


-- DB VALUES.
-- INITIAL POPULATING THE USERS TABLE

INSERT INTO the_users (FirstName, LastName, Email, DOB, City, Username, UserPassword)
VALUES ('Jake', 'Callow', 'jcal@email.com', str_to_date('05-12-1992', '%d-%m-%Y'), 'London', 'jcal', 'cat123'),
('Fred', 'Smith', 'fsmith@email.com', str_to_date('19-02-1995', '%d-%m-%Y'),'Bristol', 'freddy95', 'bristol11'),
('Hayley', 'Bieber', 'hayley99@email.com', str_to_date('01-09-1997', '%d-%m-%Y'), 'Cambridge', 'hbieber1997', 'ilovejustin1'),
('Luciano', 'Sovino', 'lucosovino89@email.com', str_to_date('02-10-1989', '%d-%m-%Y'), 'Cardiff', 'lucosov89', 'helloworld0');