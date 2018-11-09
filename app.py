import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
with open('db_details.txt', 'r') as f:
    db_details = f.readlines()
    app.config["MONGO_DBNAME"] = db_details[0]
    app.config["MONGO_URI"] = db_details[1]

mongo = PyMongo(app)