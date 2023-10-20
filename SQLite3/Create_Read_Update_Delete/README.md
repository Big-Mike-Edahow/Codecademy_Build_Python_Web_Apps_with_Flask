SQL, which stands for Structured Query Language, is a programming language designed to manage data stored in relational databases.

Once you pull the SQLite data into your Python environment, you can analyze, visualize, change, and test this data.

You may also edit a new or pre-existing SQLite database directly from a Python environment by connecting to the database using the sqlite3.connect() API.

In a database, a cursor allows us to traverse over the data one row at a time to call statements and return data. We can create a cursor object using the .cursor() method.

Using the .execute() method in combination with a CREATE clause, we can create a table within the SQLite database.

Using the .execute() method and an INSERT clause, we can insert data into a pre-existing table.
To insert multiple rows/records of data at once, we can use the .executemany() method.

To retrieve SQLite data, we can use the fetch methods; .fetchone(), .fetchmany(), and .fetchall().

A Python for loop can be used to retrieve SQLite data. It can also be used to analyze already pulled data.

After making changes to the SQLite database, we must commit the changes using the .commit() method.

When we finish editing the SQLite database commit the changes, we can use the .close() method to close the database connection.