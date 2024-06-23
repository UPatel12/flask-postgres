from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/messages', methods=['GET'])
def get_all_messages():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM messages;')
    messages = cur.fetchone()[0]
    cur.close()
    conn.close()
    return messages

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

