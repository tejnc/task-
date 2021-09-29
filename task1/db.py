import sqlite3

#creating connection with sqlite database
conn = sqlite3.connect("users.sqlite")

#creating cursor object
cursor = conn.cursor()
sql_query = """CREATE TABLE user(
    email text PRIMARY KEY,
    name text NOT NULL
)"""

#executing sql query to create table
cursor.execute(sql_query)

