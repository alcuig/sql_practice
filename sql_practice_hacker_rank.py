#BASIC SELECT

#Query all columns for all American cities in the CITY table with populations larger than 100000. 
# The CountryCode for America is USA.

select * from city where population > 100000 and countrycode = "USA";

##Query the NAME field for all American cities in the CITY table with populations larger than 120000. 
#The CountryCode for America is USA.

select name from city where population > 120000 and countrycode = "USA";

#Query all columns (attributes) for every row in the CITY table.

select * from city;

#Query all columns for a city in CITY with the ID 1661.

select * from city where ID = 1661;

#Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
select * from city where countrycode = "JPN";

#Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
select name from city where countrycode = "JPN";

#Query a list of CITY and STATE from the STATION table.
select city, state from STATION; 

#Query a list of CITY names from STATION for cities that have an even ID number. 
#Print the results in any order, but exclude duplicates from the answer.

select distinct city from station where mod(id,2) =0;

#Find the difference between the total number 
# of CITY entries in the table and the number of distinct CITY entries in the table.
SELECT COUNT(CITY) - COUNT(distinct CITY) FROM STATION;

#Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
# Your result cannot contain duplicates.
select distinct(city) from station where city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u';

#Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
select distinct city from station where city not regexp '^[a,e,i,o,u]';

#Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. 
# Your result cannot contain duplicates.

select distinct city from station where city regexp '^[a,e,i,o,u].*[a,e,i,o,u]$';

#Query the list of CITY names from STATION that do not end with vowels. 
# Your result cannot contain duplicates.
select distinct city from station where city not regexp '[a,e,i,o,u]$';

#Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. 
# Your result cannot contain duplicates.

select distinct city from station where city not regexp '^[a,e,i,o,u].*[a,e,i,o,u]$';

#Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. 
# Your result cannot contain duplicates.
select distinct city from station where city not regexp '^[a,e,i,o,u]|[a,e,i,o,u]$';

#BASIC JOIN
#Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
select sum(city.population) as 'sum_pop_city_asia' from city inner join country on city.countrycode = country.code where continent = 'Asia';

#Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
select city.name from city inner join country on city.countrycode = country.code where continent = 'Africa';

#Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
select name from Employee order by name asc;

#Write a query that prints a list of employee names (i.e.: the name attribute) 
# for employees in Employee having a salary greater than  per month who have been employees 
# for less than  months. Sort your result by ascending employee_id.
select name from employee where salary >2000 and months < 10 order by employee_id asc;

#Query the Name of any student in STUDENTS who scored higher than  Marks. 
# Order your output by the last three characters of each name. 
# If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), 
# secondary sort them by ascending ID.
select name from students where marks>75 order by right(name,3),id;

Query a count of the number of cities in CITY having a Population larger than 100000.
select count(id) from city where population > 100000;

#Query the total population of all cities in CITY where District is California.
select sum(population) from city where district = 'California';

#Query the average population of all cities in CITY where District is California.
select avg(population) from city where district = "California";

#Query the average population for all cities in CITY, rounded down to the nearest integer.
select floor(avg(population)) from city;

#Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
select sum(population) from city where countrycode = 'JPN';

#Query the difference between the maximum and minimum populations in CITY.
select max(population)-min(population) from city;

#Query the following two values from the STATION table:
# The sum of all values in LAT_N rounded to a scale of 2 decimal places.
# The sum of all values in LONG_W rounded to a scale of 2 decimal places.
select round(sum(lat_n),2), round(sum(long_w),2) from station; 