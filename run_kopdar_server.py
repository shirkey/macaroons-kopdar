#!/usr/bin/env python
# encoding: utf-8

# START 1 OMIT
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to KopDar Members site"

# END 1 OMIT

# START 2 OMIT
@app.route("/login/<id>")
def login(id):

# END 2 OMIT

if __name__ == "__main__":
    app.run()
