#!/usr/bin/python3
"""This module uses Flask and starts a web application"""


from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_hbnb():
    """Hello world for flask"""
    
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
