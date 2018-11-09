import os
import json
import time
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
with open('db_details.txt', 'r') as f:
    db_details = f.readlines()
    app.config["MONGO_DBNAME"] = db_details[0]
    app.config["MONGO_URI"] = db_details[1]

mongo = PyMongo(app)

# CALLABLE FUNCTIONS #########################################################

def read_json_data(json_file):
    """
    Read data from json file
    """
    with open(json_file, "r") as json_data:
            data = json.load(json_data)
    return data

def write_json_data(data, json_file):
    """
    Write data to json file
    """
    with open(json_file, "w") as json_data:
        json.dump(data, json_data) 


def backup_mongo_collection(collection):
    """
    Creates json backup of defined mongodb collection in
    /static/data/json/backups/ with timestamp.
    Object _id is ommitted from backup.
    Requires /static/data/json/backups/ to exist.
    """
    collection = collection.find()
    backup_json = []
    for doc in collection:
        backup_json.append(doc)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    for doc in backup_json:
        doc.pop('_id')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    backup_file_name = "static/data/json/backups/all_assets_collection_" \
                       "backup_%s.json" % timestr
    write_json_data(backup_json, backup_file_name)
    print("Back up created of 'all_assets'. Back up collection has %s"  \
           "documents." % len(backup_json))

def list_attr_values(attr, collection):
    """
    Returns sorted list of all possible values of a defined attiribute in 
    all docs in defined collection.
    """
    collection = collection.find()
    values = []
    for doc in collection:
        if attr in doc and doc[attr] != "" \
            and doc[attr] not in values:
            values.append(doc[attr])
    values.sort()
    return values

def list_attr_collection(collection):
    """
    Returns sorted list of all attributes in all docs in defined collection.
    """
    collection = collection.find()
    attr_ls = []
    for doc in collection:
        for attr in doc:
            if attr not in attr_ls:
                attr_ls.append(attr)
    attr_ls.sort()
    return attr_ls

# TEMPLATE RENDERING FUNCTIONS ###############################################

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets')
def assets():
    print()

@app.route('/trends')
def trends():
        print()

print(list_attr_collection(mongo.db.all_assets))
"""
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
"""