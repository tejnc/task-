''''
This is the 2nd api.
'''
from flask import Flask,jsonify,json,request
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("users.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn

    # if request.method == 'GET':
    #     cursor=conn.execute("SELECT * FROM user")
    #     #dict comprehension
    #     users = [dict(email=row[0],name=row[1]) for row in cursor.fetchall()]

    #     if users is not None:
    #         return jsonify(users)

@app.route('/users',methods=['GET'])
def user_list():
    conn = db_connection()
    cursor = conn.cursor()

    email_list=[]
    if request.method == 'GET':
        cursor = conn.execute("SELECT email FROM user")
        for row in cursor.fetchall():
           email_list.append(row)
        return jsonify(email_list)

if __name__ == "__main__":
    app.run(debug=True)
