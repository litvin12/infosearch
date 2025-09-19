DROP DATABASE IF EXISTS sample_database;
CREATE DATABASE sample_database;
USE sample_database;

create table sal(
   snum int(4) NOT NULL,
   sname varchar(10) NOT NULL,
   city  varchar(10) NOT NULL,
   comm  double(7,2) NOT NULL,
   PRIMARY KEY (snum));

create table cust(
   cnum int(4) NOT NULL,
   cname varchar(10) NOT NULL,
   city  varchar(10) NOT NULL,
   rating int(6) NOT NULL,
   snum int(5),
   PRIMARY KEY (cnum));

create table ord(
   onum int(4) NOT NULL,
   amt  double(7,2) NOT NULL,
   odate varchar(10) NOT NULL,
   cnum int(4),
   snum int(4),
   PRIMARY KEY (onum),
   FOREIGN KEY (cnum) REFERENCES cust(cnum),
   FOREIGN KEY (snum) REFERENCES sal(snum)
);

INSERT INTO sal (snum, sname, city, comm)
VALUES
    (1001,    "Peel",    "London", 0.12),
    (1002,  "Serres",  "San Jose", 0.13),
    (1004,  "Motica",    "London", 0.11),
    (1007,  "Rifkin", "Barcelona", 0.15),
    (1003, "Axelrod",  "New York", 0.10);

INSERT INTO cust (cnum, cname, city, rating, snum)
VALUES
    (2001,  "Hoffman",   "London", 100, 1001),
    (2002, "Giovanni",     "Rome", 200, 1003),
    (2003,      "Liu", "San Jose", 200, 1002),
    (2004,    "Grass",   "Berlin", 300, 1002),
    (2006,  "Clemens",   "London", 100, 1001),
    (2008, "Cisneros", "San Jose", 300, 1007),
    (2007,  "Pereira",     "Rome", 100, 1004);

INSERT INTO ord (onum, amt, odate, cnum, snum)
VALUES
	(3001,   18.69, STR_TO_DATE("03-10-90", "%d-%m-%Y"), 2008, 1007),
	(3003,  767.19, STR_TO_DATE("03-10-90", "%d-%m-%Y"), 2001, 1001),
	(3002, 1900.10, STR_TO_DATE("03-10-90", "%d-%m-%Y"), 2007, 1004),
	(3005, 5160.45, STR_TO_DATE("03-10-90", "%d-%m-%Y"), 2003, 1002),
	(3006, 1098.16, STR_TO_DATE("03-10-90", "%d-%m-%Y"), 2008, 1007),
	(3009, 1713.23, STR_TO_DATE("04-10-90", "%d-%m-%Y"), 2002, 1003),
	(3007,   75.75, STR_TO_DATE("04-10-90", "%d-%m-%Y"), 2004, 1002),
	(3008, 4723.00, STR_TO_DATE("05-10-90", "%d-%m-%Y"), 2006, 1001),
	(3010, 1309.95, STR_TO_DATE("06-10-90", "%d-%m-%Y"), 2004, 1002),
	(3011, 9891.88, STR_TO_DATE("06-10-90", "%d-%m-%Y"), 2006, 1001);