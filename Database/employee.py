import sqlite3 as sql
script = '''
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    BirthDate DATE,
    HireDate DATE,
    Position VARCHAR(50),
    Salary DECIMAL(10, 2)
);

INSERT INTO Employee (EmployeeID, FirstName, LastName, BirthDate, HireDate, Position, Salary)
VALUES
(1, 'John', 'Doe', '1980-01-15', '2005-06-01', 'Manager', 75000.00),
(2, 'Jane', 'Smith', '1985-03-22', '2010-08-15', 'Engineer', 68000.00),
(3, 'Michael', 'Brown', '1990-07-30', '2018-01-10', 'Technician', 45000.00),
(4, 'Emily', 'Davis', '1987-11-12', '2011-10-01', 'Accountant', 62000.00),
(5, 'David', 'Wilson', '1975-05-25', '2000-09-20', 'Director', 95000.00);
'''

with sql.Connection('learn.db') as connection:
    cur = connection.cursor()
    cur.executescript(script)
    results = cur.execute('SELECT * FROM Employee;').fetchall()
    for res in results:
        print(res)
