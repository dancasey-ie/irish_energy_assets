import os
import json
import time
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
    Creates json backup of defined collection in /static/data/json/backups/
    Object _id is ommitted from backup.
    """
    backup_json = []
    for doc in collection:
        backup_json.append(doc)
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
    all docs in defined collection. All values must be of same type.
    """
    values = []
    for doc in collection:
        if attr in doc and doc[attr] != "" \
            and doc[attr] not in values:
            if isinstance(doc[attr], str):
                values.append(doc[attr].lower())
            else:
                values.append(doc[attr])
    values.sort()
    return values

def list_attr_collection(collection):
    """
    Returns sorted list of all attributes in all docs in defined collection.
    Attributes are case sensitive.
    """
    attr_ls = []
    for doc in collection:
        for attr in doc:
            if attr not in attr_ls:
                attr_ls.append(attr)
    attr_ls.sort()
    return attr_ls

def list_attr_dict(attr, attr_to_sum, collection):
    """
    Returns sorted list of dictionaries, each dictionary correspounds to a 
    attribute value in collection. Dictionary contains attribute value, 
    number of docs with attribute value in collection and sum of MEC_MW 
    attribute for docs with attribute value.
    """
    values = ['NA']
    ls_attr_dict = [{'Name': 'NA', 'Count': 0, 'Total': 0}]
    for doc in collection:
        if attr_to_sum not in doc:
            break
        elif attr not in doc or doc[attr] == 'NA' or doc[attr] == "":
            for attr_dict in ls_attr_dict:
                if attr_dict['Name'] == 'NA':
                    attr_dict['Count'] += 1
                    attr_dict['Total'] += float(doc[attr_to_sum])
                    break
        elif isinstance(doc[attr], str) and doc[attr].title() not in values:
                attr_dict = {'Name': doc[attr].title(), 'Count': 1, 'Total': \
                             float(doc[attr_to_sum])}
                ls_attr_dict.append(attr_dict)
                values.append(doc[attr].title())
        elif not isinstance(doc[attr], str) and doc[attr] not in values:
                attr_dict = {'Name': doc[attr], 'Count': 1, 'Total': \
                             float(doc[attr_to_sum])}
                ls_attr_dict.append(attr_dict)
                values.append(doc[attr])
        else: 
                for attr_dict in ls_attr_dict:
                    if isinstance(doc[attr], str) and \
                        attr_dict['Name'] == doc[attr].title():
                        attr_dict['Count'] += 1
                        attr_dict['Total'] += float(doc[attr_to_sum])
                        break
    for attr_dict in ls_attr_dict:
        attr_dict['Total'] = round(attr_dict['Total'], 2)
    # when below is combined with above, not all Totals rounded ??
    for attr_dict in ls_attr_dict: 
        if attr_dict['Name'] == 'NA' and attr_dict['Count'] == 0:
           ls_attr_dict.remove(attr_dict)
           values.remove('NA')

    ls_attr_dict_sorted = [x for y,x in sorted(zip(values, ls_attr_dict), \
        key=lambda pair: pair[0])]
    return ls_attr_dict_sorted 

def sort_collection(attr, reverse, collection):
    """
    Sorts a collection based on attribute.
    Case sensitive.
    """
    collection_ls = []
    attr_value_ls = []
    for doc in collection:
        attr_value_ls.append(doc[attr])
        collection_ls.append(doc)
    collection_sorted = [x for y,x in sorted(zip(attr_value_ls,
                                                 collection_ls) \
        ,key=lambda pair: pair[0], reverse=reverse)]
    return collection_sorted 

def get_total(attr, collection):
    """
    Returns sum of values of defined attribute in defined collection.
    """
    total = 0
    for doc in collection:
        if attr in doc:
            total += float(doc[attr])
    return round(total, 2)

def search_collection(keyword, collection):
    """
    Collection filter for keyword.
    Returns subset of defined collection that contains the defined
    keyword in its attribute values.
    """
    keyword = keyword.lower()
    if keyword == "" or keyword == " ":
        return collection
    else:
        flt_collection = []
        for doc in collection:
            for attr in doc:
                if attr != '_id' and keyword in str(doc[attr]).lower():
                    flt_collection.append(doc)
                    break          
        return flt_collection

def filter_collection(attr, values, collection):
    """
    Collection filter for attribute list of values.
    Returns subset of collection that defined attribute's value is in defined list
    of values.
    """
    flt_collection = []
    for doc in collection:
        if attr in doc:
            for value in values:     
                if str(doc[attr]).lower() == str(value).lower() or \
                    (doc[attr] == '' and 'NA' in values):
                    flt_collection.append(doc)
        elif 'NA' in values:
            flt_collection.append(doc)

    return flt_collection

def filter_attr_range(attr, lo, hi, collection):
    """
    Collection filter for attribute value within range.
    Returns subset of collection that defined attribute's value is between
    defined range set by hi and lo constraints.
    """
    flt_collection = []
    for doc in collection:
        if attr in doc and float(doc[attr]) >= lo and float(doc[attr]) <= hi:
            flt_collection.append(doc)
    return flt_collection

# TEMPLATE RENDERING FUNCTIONS ###############################################

@app.route('/')
def index():
    return render_template('index.html',
                           username="")

@app.route('/assets')
def assets():
    attributes = read_json_data('static/data/json/relevent_attributes.json')
    all_assets = mongo.db.all_assets.find()
    statuses = list_attr_dict('Status', "MEC_MW", mongo.db.all_assets.find())
    system_operators = list_attr_dict('SystemOperator', "MEC_MW",
                                      mongo.db.all_assets.find())
    types = list_attr_dict('Type', "MEC_MW", mongo.db.all_assets.find())
    nodes = list_attr_dict('Node', "MEC_MW", mongo.db.all_assets.find())
    counties = list_attr_dict('County', "MEC_MW", mongo.db.all_assets.find())
    jurisdictions = list_attr_dict('Jurisdiction', "MEC_MW", mongo.db.all_assets.find())
    assets = sort_collection('Name', False, mongo.db.all_assets.find())
    mec_total = get_total('MEC_MW', assets)

    return render_template("assets.html", 
                           assets=assets,
                           attributes=attributes,
                           doc_count=len(assets),
                           mec_total=mec_total,
                           statuses=statuses,
                           system_operators=system_operators,
                           types=types,
                           nodes=nodes,
                           counties=counties,
                           jurisdictions=jurisdictions,
                           username="")

@app.route('/filtered_assets', methods=['POST'])
def filtered_assets():
    doc_sort = request.form['doc_sort']
    flt_search = (request.form['flt_search']).lower()
    flt_status = request.form.getlist('flt_status')
    flt_system_operator = request.form.getlist('flt_system_operator')
    flt_type = request.form.getlist('flt_type')
    flt_mec_lo = float(request.form['flt_mec_lo'])
    flt_mec_hi = float(request.form['flt_mec_hi'])
    flt_node = request.form.getlist('flt_node')
    flt_county = request.form.getlist('flt_county')
    flt_jurisdiction = request.form.getlist('flt_jurisdiction')
    assets = mongo.db.all_assets.find()
    attributes = read_json_data('static/data/json/relevent_attributes.json')
    if doc_sort == "0":
        assets = sort_collection('Name', False, assets)
    elif doc_sort == "1":
        assets = sort_collection('Name', True, assets)
    elif doc_sort == "2":
        assets = sort_collection('Type', False, assets)
    elif doc_sort == "3":
        assets = sort_collection('Type', True, assets)
    elif doc_sort == "4":
        assets = sort_collection('MEC_MW', False, assets)
    elif doc_sort == "5":
        assets = sort_collection('MEC_MW', True, assets)
    if flt_search != "":
        assets = search_collection(flt_search, assets)
    if flt_status != []:
        assets = filter_collection('Status', flt_status, assets)
    if flt_system_operator != []:
        assets = filter_collection('SystemOperator',
                                   flt_system_operator,
                                   assets)
    if flt_type != []:
        assets = filter_collection('Type', flt_type, assets)
    assets = filter_attr_range('MEC_MW', flt_mec_lo, flt_mec_hi, assets)
    if flt_node != []:
        assets = filter_collection('Node', flt_node, assets)
    if flt_county != []:
        assets = filter_collection('County', flt_county, assets)
    if flt_jurisdiction != []:
        assets = filter_collection('Jurisdiction', flt_jurisdiction, assets)
    statuses = list_attr_dict('Status', "MEC_MW", assets)
    system_operators = list_attr_dict('SystemOperator', "MEC_MW", assets)
    types = list_attr_dict('Type', "MEC_MW", assets)
    nodes = list_attr_dict('Node', "MEC_MW", assets)
    counties = list_attr_dict('County', "MEC_MW", assets)
    jurisdictions = list_attr_dict('Jurisdiction', "MEC_MW", mongo.db.all_assets.find())
    mec_total = get_total('MEC_MW', assets)


    return render_template("assets.html", 
                           assets=assets,
                           attributes=attributes,
                           doc_count=len(assets),
                           mec_total=mec_total,
                           statuses=statuses,
                           system_operators=system_operators,
                           types=types,
                           nodes=nodes,
                           counties=counties,
                           jurisdictions=jurisdictions,
                           username="")

@app.route('/log_in')
def log_in():
    return render_template("log_in.html",
                           username="",
                           message="")
@app.route('/log_out')
def log_out():
    return render_template('index.html',
                           username="") 

@app.route('/check_username', methods=['POST'])
def check_username():
    """
    Module accepts POST of username from log_in.html.
    Return filtered assets.html or appropriete message on log_in.html.
    """

    if request.method == "POST":
        username = request.form["username"]
        users = read_json_data("data/users.json")
        attributes = read_json_data('static/data/json/relevent_attributes.json')
        if username not in users:
            message = "That is not a valid username."
            return render_template("log_in.html",
                                   message=message,
                                   username="")
        elif username == 'admin':
            assets = sort_collection('Name', False, mongo.db.all_assets.find())
        else:
            assets = filter_collection('Company', [username], mongo.db.all_assets.find())
        statuses = list_attr_dict('Status', "MEC_MW", assets)
        system_operators = list_attr_dict('SystemOperator', "MEC_MW",assets)
        types = list_attr_dict('Type', "MEC_MW", assets)
        nodes = list_attr_dict('Node', "MEC_MW", assets)
        counties = list_attr_dict('County', "MEC_MW", assets)
        jurisdictions = list_attr_dict('Jurisdiction', "MEC_MW", assets)
        assets = sort_collection('Name',False,assets)
        mec_total = get_total('MEC_MW', assets)
            
        return render_template("assets.html",
                                assets=assets,
                                attributes=attributes,
                                doc_count=len(assets),
                                mec_total=mec_total,
                                statuses=statuses,
                                system_operators=system_operators,
                                types=types,
                                nodes=nodes,
                                counties=counties,
                                jurisdictions=jurisdictions,
                                username=username)


@app.route('/trends')
def trends():
    assets = mongo.db.all_assets.find()
    assets = list(assets)
    for doc in assets:
        doc.pop('_id')
    write_json_data(assets, 'static/data/json/assets.json')
    return render_template('trends.html',
                           assets=assets)

@app.route('/new_asset')
def new_asset():
    return render_template('add_asset.html')

@app.route('/add_asset', methods=['POST'])
def add_asset():
    asset_db = mongo.db.all_assets.find()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    asset_doc = {"Name": request.form['Name'],
                 "Type":  request.form['Type'],
                 "MEC_MW":  request.form['MEC_MW'],
                 "GenRef":  request.form['GenRef'],
                 "Company":  request.form['Company'],
                 "Node":  request.form['Node'],
                 "NodeAddress":  request.form['NodeAddress'],
                 "NodeVoltage":  request.form['NodeVoltage'],
                 "SystemOperator":  request.form['SystemOperator'],
                 "AssetAddress":  request.form['AssetAddress'],
                 "Status":  request.form['Status'],
                 "FirstAdded": timestr
                 }
    mongo.db.all_assets.insert_one(asset_doc)
    
    return redirect(url_for('assets'))

@app.route('/edit_asset/<asset_id>')
def edit_asset(asset_id):
    assets = mongo.db.all_assets.find()
    attributes = list_attr_collection(assets)
    types = list_attr_values('Type', mongo.db.all_assets.find())
    counties = read_json_data('static/data/json/Irish_Counties.json')
    asset=mongo.db.all_assets.find_one({'_id': ObjectId(asset_id)})
    node_address = asset['NodeAddress']
    node_address_ls = list(node_address.split(",")) 
    return render_template('edit_asset.html',
                           types=types,
                           counties=counties,
                           attributes=attributes,
                           asset=asset,
                           node_address_ls= node_address_ls,
                           username=username)

@app.route('/update_asset/<asset_id>', methods=['POST'])
def update_asset(asset_id):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    mongo.db.all_assets.update(
                {'_id': ObjectId(asset_id)},
                {"Name": request.form['Name'],
                 "Type":  request.form['Type'],
                 "MEC_MW":  request.form['MEC_MW'],
                 "GenRef":  request.form['GenRef'],
                 "Company":  request.form['Company'],
                 "Node":  request.form['Node'],
                 "NodeAddress":  request.form['NodeAddress'],
                 "NodeVoltage":  request.form['NodeVoltage'],
                 "SystemOperator":  request.form['SystemOperator'],
                 "AssetAddress":  request.form['AssetAddress'],
                 "Status":  request.form['Status'],
                 "LastUpdated": timestr})
                 
    return redirect(url_for('assets'))
    
@app.route('/delete_asset/<asset_id>')  
def delete_asset(asset_id):
    mongo.db.all_assets.remove({'_id': ObjectId(asset_id)})
    return redirect(url_for("assets"))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

