from os import name
from flask import Flask, json, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('users.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

#According to specification this only needs post method
@app.route('/user',methods=['GET','POST'])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor=conn.execute("SELECT * FROM user")
        #dict comprehension
        users = [dict(email=row[0],name=row[1]) for row in cursor.fetchall()]

        if users is not None:
            return jsonify(users)


    if request.method == 'POST':
        new_email = request.form['email']
        new_name = request.form['name']

        sql="""INSERT INTO user(email,name) VALUES(?,?)"""
        cursor = cursor.execute(sql,(new_email,new_name))
        conn.commit()
        return f"{new_email} has been created successfully."
