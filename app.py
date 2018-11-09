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

def list_attr_dict(attr, collection):
    """
    Returns list of dictionaries, each dictionary correspounds to a attribute 
    value in collection. Dictionary contains attribute value, number of docs 
    with attribute value in collection and sum of MEC_MW attribute for docs with
    attribute value.
    """
    collection = collection.find()
    values = ['NA']
    ls_attr_dict = [{'Name': 'NA', 'Count': 0, 'MEC_Sum': 0}]
    for doc in collection:
        if attr not in doc or doc[attr] == 'NA' or doc[attr] == "":
            for attr_dict in ls_attr_dict:
                if attr_dict['Name'] == 'NA':
                    attr_dict['Count'] += 1
                    attr_dict['MEC_Sum'] += doc['MEC_MW']
                    break
        elif doc[attr] not in values:
                attr_dict = {'Name': doc[attr], 'Count': 1, 'MEC_Sum': doc['MEC_MW']}
                ls_attr_dict.append(attr_dict)
                values.append(doc[attr])
        else: 
                for attr_dict in ls_attr_dict:
                    if attr_dict['Name'] == doc[attr]:
                        attr_dict['Count'] += 1
                        attr_dict['MEC_Sum'] += doc['MEC_MW']
                        break
    for attr_dict in ls_attr_dict:
        attr_dict['MEC_Sum'] = round(attr_dict['MEC_Sum'], 2)
    for attr_dict in ls_attr_dict: # when combined with above, not all MEC_Sum's rounded ??
        if attr_dict['Name'] == 'NA' and attr_dict['Count'] == 0:
           ls_attr_dict.remove(attr_dict)
           values.remove('NA')

    ls_attr_dict_sorted = [x for y,x in sorted(zip(values, ls_attr_dict), key=lambda pair: pair[0])]
    return ls_attr_dict_sorted 

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

print(list_attr_dict('Type', mongo.db.all_assets))

"""
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
"""