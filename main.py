import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')



'''part 1 '''
employees = pd.read_sql("""
SELECT *
 FROM employees;
""", conn)

print(employees)

# 1. Select all of the employees with the first name "Leslie"
pd.read_sql("""
SELECT *
 FROM employees
WHERE firstName = "Leslie";
""", conn)

# 2. For the employees named Leslie, give the first name, last name, and job title.
pd.read_sql("""
SELECT firstName, lastName, jobTitle
 FROM employees
WHERE firstName = "Leslie";
""", conn)

# 3. Select all employees who have a last name with fewer than 5 characters. Using inequalities, do this in two different ways using conditionals.
pd.read_sql("""
SELECT *, length(lastName) AS name_length
 FROM employees
WHERE name_length < 5;
""", conn)

# OR

# Less than or equal to 4.
pd.read_sql("""
SELECT *, length(lastName) AS name_length
 FROM employees
WHERE name_length <= 4;
""", conn)





'''part 2'''
orderDetails = pd.read_sql("""
SELECT *
FROM orderDetails;
""", conn)

print(orderDetails)

# 4. Round the price as an integer.
pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS rounded_price_int
 FROM orderDetails
WHERE rounded_price_int >= 100;
""", conn)






'''part 3 Let's look at the orders database.'''
orders = pd.read_sql("""
SELECT *
 FROM orders;
""", conn)

print(orders)

# 5. Find all orders placed in the year 2005 in the orders database.
pd.read_sql("""
SELECT *, strftime("%Y", orderDate) AS year
 FROM orders
WHERE year = "2005";
""", conn)

# 6. Going back to the employees database, use LIKE to find all of those who have "sale" or "sales" in their job title.
pd.read_sql("""
SELECT *
 FROM employees
WHERE jobTitle LIKE "Sale%";
""", conn)

# 7. Find out how many items are priced at least $200 in the orderDetails database.
pd.read_sql("""
SELECT COUNT(priceEach)
 FROM orderDetails
WHERE priceEach >=200;
""", conn)

conn.close()