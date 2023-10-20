# insert_multiple_rows.py
# insert a list of tuples into a database

import sqlite3

con = sqlite3.connect("titanic.db")
curs = con.cursor()

# Here is the new_rows object
new_rows = [('Anne Smith', 33, 'AS896', 25.00),
            ('Billy Roberts', 29, 'bill5Rob', 30.00),
            ('Jason Johnson', 48, 'JasonJ77', 40.00),
            ('Tim Trunk', 51, 'Timtrunk4', 40.00),
            ('Sarah Fall',19, 'SFall232', 25.00)
            ]

# Insert new_rows into the new_table table
curs.executemany('''INSERT INTO new_table VALUES (?,?,?,?)''', new_rows)






