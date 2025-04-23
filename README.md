# Practice for Filtering with SQL

## Instructions

### Set Up

* Fork and Clone the GitHub Repo
* Install dependencies and enter the virtual environment:
    * `pipenv install`
    * `pipenv shell`

Next, let's set up our code in `main.py`. Import libraries and connect to the database.

```python
# Add to main.py

import pandas as pd
import sqlite3

conn = sqlite3.connect('data.sqlite')
```
## Employees Table Queries

Take a look at the employees table.

```python
employees = pd.read_sql("""
SELECT *
  FROM employees;
""", conn)

print(employees)
```

1. Select all of the employees with first name "Leslie"

2. For the employees named Leslie, give the first name, last name, and job title.

3. Select all employees that have a last name less than 5. Using inequalities, do this in two different ways using conditionals.

## OrderDetails Table Queries

Now let's turn to the orderDetails table.

```python
# Add this code to orderDetails table
order_details = pd.read_sql("""
SELECT *
  FROM orderDetails;
""", conn)

print(order_details)
```

4. Round the price as an integer

## Orders Table Queries

Let's look at the orders table.

```python
orders = pd.read_sql("""
SELECT *
  FROM orders;
""", conn)

print(orders)
```

5. Find all orders placed in the year 2005 in the orders database.

6. Going back to the employees database, use LIKE to find all of those who have sale or sales in their job title.

7. Now find out how many items are priced at least $200 in the orderDetails database.