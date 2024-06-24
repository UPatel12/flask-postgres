from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
"""
The "/" endpoint fetches the first entry in the DB
"""
@app.route('/')
def get_message():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT content FROM messages LIMIT 1;')
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return message

"""
The "/messages" endpoint fetches all the entries in the DB
"""

@app.route('/messages', methods=['GET'])
def get_all_messages():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM messages;')
    messages = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

