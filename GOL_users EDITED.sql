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


INSERT INTO the_users (UserID, FirstName, LastName, Email, DOB, City, Username, UserPassword)
VALUES (1, 'Jake', 'Callow', 'jcal@email.com', str_to_date('05-12-1992', '%d-%m-%Y'), 'London', 'cobrien1', 'cat123'),
(2, 'Fred', 'Smith', 'fsmith@email.com', 1995-02-19, 'Bristol', 'freddy95', 'bristol11'),
(3, 'Hayley', 'Bieber', 'hayley99@email.com', 1997-09-01, 'Cambridge', 'hbieber1997', 'ilovejustin1'),
(4, 'Luciano', 'Sovino', 'lucosovino89@email.com', 1989-10-29, 'Cardiff', 'lucosov89', 'helloworld0');


"""-------------------------------TO BE REVIEWED -------------------------------------------"
-- UPDATED CODE BELOW.
-- SQL Code to create database for users
-- AUTO INCREMENT ADDED

START TRANSACTION;
CREATE DATABASE GOL_users;
USE GOL_users;

CREATE TABLE the_users (
    UserID int(10) AUTO_INCREMENT,
    FirstName varchar(65),
	LastName varchar(65),
    Email varchar(65) UNIQUE,
    DOB DATE,
    City varchar(65),
    Username varchar(65) UNIQUE,
	UserPassword varchar(65),
    PRIMARY KEY (UserID)
);


CREATE TABLE searched_words (
    word varchar(50) NOT NULL,
    definition_ varchar(6000) NOT NULL
);

CREATE TABLE user_streaks(
	Username VARCHAR(65),
    StreaksID Int AUTO_INCREMENT,
	LastLogin DATE,
	UserStreak Int,
    PRIMARY KEY (StreaksID),
	FOREIGN KEY (Username) REFERENCES the_users(Username),
	FOREIGN KEY (Email) REFERENCES the_users(Email)

);

INSERT INTO the_users (FirstName, LastName, Email, DOB, City, Username, UserPassword)
VALUES ('Jake', 'Callow', 'jcal@email.com', str_to_date('05-12-1992', '%d-%m-%Y'), 'London', 'cobrien1', 'cat123'),
('Fred', 'Smith', 'fsmith@email.com', str_to_date('19-02-1995', '%d-%m-%Y'),'Bristol', 'freddy95', 'bristol11'),
('Hayley', 'Bieber', 'hayley99@email.com', str_to_date('01-09-1997', '%d-%m-%Y'), 'Cambridge', 'hbieber1997', 'ilovejustin1'),
('Luciano', 'Sovino', 'lucosovino89@email.com', str_to_date('02-10-1989', '%d-%m-%Y'), 'Cardiff', 'lucosov89', 'helloworld0');


-- INSERTING VALUES INTO THE USER STREAKS TABLE.
-- TO BE ADJUSTED AS I NEED THE FOREIGN KEYS TO EXTRACT INFORMATION FROM THE PRIMARY LOCATIONS.

--INSERT INTO user_streaks (Username)
--SELECT
--Username
--FROM the_users;

--UPDATE user_streaks
--SET LastLogin = str_to_date('25-10-2022', '%d-%m-%Y'), UserStreak = 2
--WHERE Username = 'cobrien1';
--
--UPDATE user_streaks
--SET LastLogin = str_to_date('20-10-2022', '%d-%m-%Y'), UserStreak = 6
--WHERE Username = 'hbieber1997';


-- VIEWING THE TABLES.
SELECT * FROM the_users;
SELECT * FROM user_streaks;