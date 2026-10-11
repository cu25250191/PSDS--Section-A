
import sqlite3

# Connect to database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Enable foreign key
cursor.execute("PRAGMA foreign_keys = ON")

# Create Department table
cursor.execute("""
CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
)
""")

# Create Employee table
cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id)
    REFERENCES departments(dept_id)
)
""")

# Insert Department records
departments = [
    (1, "HR"),
    (2, "IT"),
    (3, "Accountant")
]

cursor.executemany(
    "INSERT INTO departments VALUES (?, ?)",
    departments
)

# Insert Employee records
employees = [
    (1, "Vansh Saini", 1),
    (2, "Rishabh Tiwari", 2),
    (3, "Kartik Saini", 2),
    (4, "Neha Verma", 3),
    (5, "Rohit Kumar", 3)
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?)",
    employees
)

conn.commit()

# Display Department table
print("DEPARTMENT TABLE")
cursor.execute("SELECT * FROM departments")
for row in cursor.fetchall():
    print(row)

# Display Employee table
print("\nEMPLOYEE TABLE")
cursor.execute("SELECT * FROM employees")
for row in cursor.fetchall():
    print(row)

# Join both tables
print("\nEMPLOYEE DETAILS WITH DEPARTMENT")
cursor.execute("""
SELECT employees.emp_id, employees.emp_name,
       departments.dept_name
FROM employees
JOIN departments
ON employees.department_id = departments.dept_id
""")

for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
