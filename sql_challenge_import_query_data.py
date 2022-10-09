#Challenge : Import and Query data

#Import data into the human_resources.departments table.
#Import data into the human_resources.employees table.
#CSV files use UTF8 encoding, including headers, and use the comma delimiter character.
#Write a query that returns employees in the South building. 

#PART 1 - Creating the tables headers and value types based on csv files. 

CREATE TABLE human_resources.departments (
    department_id integer PRIMARY KEY,
    department_name varchar(50),
    building varchar(50)
);

CREATE TABLE human_resources.employees (
    employee_id integer,
    first_name varchar(50),
    last_name varchar(50),
    hire_date varchar(50),
    department_id integer,
    FOREIGN KEY (department_id ) REFERENCES human_resources.departments(department_id)
);
--
#PART 2 - Importing the data from the csv into the tables, using 3 possible methods:

#1. GUI (Pgadmin, DBeaver)

#2. PSQL
COPY human_resources.departments(department_id, department_name, building)
FROM '/Users/alyssacuignet/Downloads/Ex_Files_PostgreSQL_EssT/Exercise Files/Chapter 4/KinetEco-Departments.csv'
DELIMITER ','
CSV HEADER;

COPY human_resources.employees(employee_id, first_name, last_name, hire_date, department_id)
FROM '/Users/alyssacuignet/Downloads/Ex_Files_PostgreSQL_EssT/Exercise Files/Chapter 4/KinetEco-Employees.csv'
DELIMITER ','
CSV HEADER;


#3. Python(psycopg2)
import csv 
import psycopg2

#Step 1: read the data from the csv file and transform into a format (list of dictionaries)
# that can be used by the psycopg2 package to load the data into the postgres database.

def read_data(file_path):
    """
    Reads data from source .csv file and converts into a list of dictionaries.
    Format : [{column1:row1_value, column2:row1_value}, {column1: row2_value, column2: row2_value}]
    """
    header = []
    rows = []
    with open(file_path, "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    data = []
    for row in rows:
        line = {}
        for i in range(len(header)):
            line[header[i]] = row[i]
        data.append(line)
    return data

data_department = read_data("/Users/alyssacuignet/Downloads/Ex_Files_PostgreSQL_EssT/Exercise Files/Chapter 4/KinetEco-Departments.csv")
data_employees = read_data("/Users/alyssacuignet/Downloads/Ex_Files_PostgreSQL_EssT/Exercise Files/Chapter 4/KinetEco-Employees.csv")

#Step 2: Connect to postgres database.
conn = psycopg2.connect("host=localhost dbname=git_practice user=alyssacuignet")
cur = conn.cursor()


for record in data_department:
    postgres_insert_query = f""" 
        INSERT INTO human_resources.departments (
            department_id,
            department_name,
            building)
            VALUES (%s,%s,%s)
        """

    record_to_insert = (
        record["department_id"],
        record["department_name"],
        record["building"]
        )

    cur.execute(postgres_insert_query, record_to_insert)


for record in data_employees:
    postgres_insert_query_2 = f""" 
        INSERT INTO human_resources.employees (
        employee_id,
        first_name,
        last_name,
        hire_date,
        department_id)
        VALUES (%s,%s,%s,%s,%s)
        """

    record_to_insert_2 = (
        record["\ufeffemployee_id"],
        record["first_name"],
        record["last_name"],
        record["hire_date"],
        record["department_id"]
        )

    cur.execute(postgres_insert_query_2, record_to_insert_2)

conn.commit()

    


--
#PART 3 - Querying the data
CREATE VIEW employees_buildings AS
SELECT human_resources.departments.department_name, human_resources.departments.building, 
human_resources.employees.first_name, 
human_resources.employees.last_name
FROM human_resources.departments FULL JOIN human_resources.employees
ON human_resources.departments.department_id = human_resources.employees.department_id
WHERE building = 'South';

