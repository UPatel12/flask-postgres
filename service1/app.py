from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def get_message():
    response = requests.get('http://service2:5002/')
    return response.text

@app.route('/')
def get_message():
    response = requests.get('http://service2:5002/messages')
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
