CREATE TABLE EmpDetails (
    EmployeeId integer,
    EmployeeName varchar(50)
);

INSERT INTO EmpDetails(
    EmployeeId, 
    EmployeeName
) VALUES 
    (1, 'John'),
    (2, 'Samantha'),
    (3, 'Hakuna'), 
    (4, 'Silky'), 
    (5, 'Ram'), 
    (6, 'Arpit'), 
    (7, 'Lily'), 
    (8, 'Sita'), 
    (9, 'Farah'),
    (10, 'Jerry');     


CREATE TABLE EmpSalary(
    EmployeeId integer,
    EmployeeName varchar(50),
    EmployeeSalary integer
    );

INSERT INTO EmpSalary(
    EmployeeId, 
    EmployeeName, 
    EmployeeSalary
) VALUES 
    (1, 'John', 50000),
    (2, 'Samantha', 120000),
    (3, 'Hakuna', 75000), 
    (4, 'Silky', 25000), 
    (5, 'Ram', 150000), 
    (6, 'Arpit', 80000), 
    (11, 'Rose', 90000), 
    (12, 'Sakshi', 45000), 
    (13, 'Jack' ,250000);

#INNER JOIN, WHICH RETURNS RECORDS THAT HAVE MATCHING VALUES IN BOTH TABLES

#QUERY
SELECT EmpDetails. EmployeeID, EmpDetails. EmployeeName, EmpSalary. EmployeeSalary
FROM EmpDetails INNER JOIN EmpSalary #tables you want to join
ON EmpDetails. EmployeeID = EmpSalary. EmployeeID; #common column

#RESULT
 employeeid | employeename | employeesalary 
------------+--------------+----------------
          1 | John         |          50000
          2 | Samantha     |         120000
          3 | Hakuna       |          75000
          4 | Silky        |          25000
          5 | Ram          |         150000
          6 | Arpit        |          80000

#PERFORMING A LEFT OUTER JOIN, WHICH RETURNS ALL RECORDS FROM THE LEFT TABLE, AND MATCHED RECORDS FROM RIGHT TABLE

#QUERY
SELECT EmpDetails. EmployeeID, EmpDetails. EmployeeName, EmpSalary. EmployeeSalary
FROM EmpDetails LEFT JOIN EmpSalary
ON EmpDetails. EmployeeID = EmpSalary. EmployeeID;

#RESULT
 employeeid | employeename | employeesalary 
------------+--------------+----------------
          1 | John         |          50000
          2 | Samantha     |         120000
          3 | Hakuna       |          75000
          4 | Silky        |          25000
          5 | Ram          |         150000
          6 | Arpit        |          80000
          7 | Lily         |               
          8 | Sita         |               
          9 | Farah        |               
         10 | Jerry        |  

#RGHT OUTER JOIN, WHICH RETURNS ALL RECORDS FROM THE RIGHT TABLE, AND MATCHED RECORDS FROM LEFT TABLE

#QUERY
SELECT EmpDetails. EmployeeID, EmpDetails. EmployeeName, EmpSalary. EmployeeSalary
FROM EmpDetails RIGHT JOIN EmpSalary
ON EmpDetails. EmployeeID = EmpSalary. EmployeeID;

#RESULT
 employeeid | employeename | employeesalary 
------------+--------------+----------------
          1 | John         |          50000
          2 | Samantha     |         120000
          3 | Hakuna       |          75000
          4 | Silky        |          25000
          5 | Ram          |         150000
          6 | Arpit        |          80000
            |              |          90000
            |              |          45000
            |              |         250000

#FULL (OUTER) JOIN, WHICH RETURNS RECORDS WHERE THERE IS A MATCH IN EITHER LEFT OR RIGHT TABLE
#done when you want all the data from both tables, irrespective of whether there is a match or not

#QUERY
SELECT *
FROM EmpDetails FULL JOIN EmpSalary
ON EmpDetails. EmployeeID = EmpSalary. EmployeeID;

#RESULT
 employeeid | employeename | employeeid | employeename | employeesalary 
------------+--------------+------------+--------------+----------------
          1 | John         |          1 | John         |          50000
          2 | Samantha     |          2 | Samantha     |         120000
          3 | Hakuna       |          3 | Hakuna       |          75000
          4 | Silky        |          4 | Silky        |          25000
          5 | Ram          |          5 | Ram          |         150000
          6 | Arpit        |          6 | Arpit        |          80000
          7 | Lily         |            |              |               
          8 | Sita         |            |              |               
          9 | Farah        |            |              |               
         10 | Jerry        |            |              |               
            |              |         11 | Rose         |          90000
            |              |         12 | Sakshi       |          45000
            |              |         13 | Jack         |         250000

