# commit_and_close.py
# Committing changes and closing the database connection

import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# insert a row in new_table table
curs.execute('''INSERT INTO new_table VALUES ('Stephanie Bready', 37, 'stephB423', 30.00)''')

# commit this change
con.commit()
# close the connection
con.close()
