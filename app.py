import os
import json
import time
import copy
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
    backup_file_name = ("static/data/json/backups/assets_backup_%s.json"
                        % timestr)
    write_json_data(backup_json, backup_file_name)

def overwrite_with_backup(local_collection, mongo_collection):
    """
    Backs up collection locally, deletes entire mongo_collection and
    then fills it with a defined local_collection.
    """
    backup_mongo_collection(mongo_collection.find())
    result = mongo_collection.delete_many({ })
    for doc in local_collection:
        mongo_collection.insert_one(doc)

def list_attr_values(attr, collection):
    """
    Returns sorted list of all possible values of a defined attiribute in
    all docs in defined collection. All values must be of same type.
    """
    values = []
    for doc in collection:
        if attr in doc and doc[attr] != "" and isinstance(doc[attr], str) \
            and doc[attr].lower() not in values:
                    values.append(doc[attr].lower())
        elif attr in doc and doc[attr] != "" and doc[attr] not in values:
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
                attr_dict = {'Name': doc[attr].title(), 'Count': 1, 'Total':
                             float(doc[attr_to_sum])}
                ls_attr_dict.append(attr_dict)
                values.append(doc[attr].title())
        elif not isinstance(doc[attr], str) and doc[attr] not in values:
                attr_dict = {'Name': doc[attr], 'Count': 1, 'Total':
                             float(doc[attr_to_sum])}
                ls_attr_dict.append(attr_dict)
                values.append(doc[attr])
        else:
                for attr_dict in ls_attr_dict:
                    if isinstance(doc[attr], str) and \
                            attr_dict['Name'] == doc[attr].title():
                                    attr_dict['Count'] += 1
                                    attr_dict['Total'] += \
                                        float(doc[attr_to_sum])
                                    break
    for attr_dict in ls_attr_dict:
        attr_dict['Total'] = round(attr_dict['Total'], 2)
    # when below is combined with above, not all Totals rounded ??
    for attr_dict in ls_attr_dict:
        if attr_dict['Name'] == 'NA' and attr_dict['Count'] == 0:
            ls_attr_dict.remove(attr_dict)
            values.remove('NA')

    ls_attr_dict_sorted = [x for y, x in sorted(zip(values, ls_attr_dict),
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
    collection_sorted = [x for y, x in sorted(zip(attr_value_ls,
                                                  collection_ls),
                                              key=lambda pair: pair[0],
                                              reverse=reverse)]
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
    Returns subset of collection that defined attribute's value is in
    defined list of values.
    """
    flt_collection = []
    for doc in collection:
        if attr in doc:
            for value in values:
                if str(doc[attr]).lower() == str(value).lower() \
                        or (doc[attr] == '' and 'NA' in values):
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
    """
    Renders index.html with all assets.
    """
    return assets('')


@app.route('/<username>')
def assets(username):
    """
    Renders index.html with all assets.
    """

    attributes = read_json_data('static/data/json/relevent_attributes.json')
    all_assets = mongo.db.all_assets.find()
    statuses = list_attr_dict('Status', "MEC_MW", mongo.db.all_assets.find())
    system_operators = list_attr_dict('SystemOperator', "MEC_MW",
                                      mongo.db.all_assets.find())
    types = list_attr_dict('Type', "MEC_MW", mongo.db.all_assets.find())
    nodes = list_attr_dict('Node', "MEC_MW", mongo.db.all_assets.find())
    counties = list_attr_dict('County', "MEC_MW", mongo.db.all_assets.find())
    companies = list_attr_dict('Company', "MEC_MW", mongo.db.all_assets.find())
    assets = sort_collection('Name', False, mongo.db.all_assets.find())
    mec_total = get_total('MEC_MW', assets)
    assets_json = copy.deepcopy(assets)
    for doc in assets_json:
        doc.pop('_id')
    return render_template("index.html",
                           assets=assets,
                           attributes=attributes,
                           doc_count=len(assets),
                           total_docs_count=len(assets),
                           mec_total=mec_total,
                           statuses=statuses,
                           system_operators=system_operators,
                           types=types,
                           nodes=nodes,
                           counties=counties,
                           companies=companies,
                           username=username,
                           assets_json=assets_json,

                           title="Irish Energy Assets | Assets")

@app.route('/filtered_assets/', methods=['POST'])
def filter_nologin():
    return filtered_assets('')

@app.route('/filtered_assets/<username>', methods=['POST'])
def filtered_assets(username):
    """
    Renders index.html with filtered assets.
    """
    doc_sort = request.form['doc_sort']
    flt_search = (request.form['flt_search']).lower()
    flt_status = request.form.getlist('flt_status')
    flt_system_operator = request.form.getlist('flt_system_operator')
    flt_type = request.form.getlist('flt_type')
    flt_mec_lo = float(request.form['flt_mec_lo'])
    flt_mec_hi = float(request.form['flt_mec_hi'])
    flt_node = request.form.getlist('flt_node')
    flt_county = request.form.getlist('flt_county')
    flt_company = request.form.getlist('flt_company')
    assets = mongo.db.all_assets.find()
    total_docs_count = assets.count()
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
    if flt_company != []:
        assets = filter_collection('Company', flt_company, assets)
    statuses = list_attr_dict('Status', "MEC_MW", assets)
    system_operators = list_attr_dict('SystemOperator', "MEC_MW", assets)
    types = list_attr_dict('Type', "MEC_MW", assets)
    nodes = list_attr_dict('Node', "MEC_MW", assets)
    counties = list_attr_dict('County', "MEC_MW", assets)
    companies = list_attr_dict('Company', "MEC_MW", assets)
    mec_total = get_total('MEC_MW', assets)
    assets_json = copy.deepcopy(assets)
    for doc in assets_json:
        doc.pop('_id')
    return render_template("index.html",
                           assets=assets,
                           attributes=attributes,
                           doc_count=len(assets),
                           total_docs_count=total_docs_count,
                           mec_total=mec_total,
                           statuses=statuses,
                           system_operators=system_operators,
                           types=types,
                           nodes=nodes,
                           counties=counties,
                           companies=companies,
                           username=username,
                           assets_json=assets_json,
                           title="Irish Energy Assets | Assets")

@app.route('/about')
def about():
    """
    Renders about.html.
    """
    assets = list(mongo.db.all_assets.find())
    assets_json = copy.deepcopy(assets)
    for doc in assets_json:
        doc.pop('_id')
    return render_template('about.html',
                           username="",
                           assets_json=assets_json,
                           title="Irish Energy Assets | About")

@app.route('/log_in')
def log_in():
    """
    Renders log_in.html.
    """
    return render_template("log_in.html",
                           username="",
                           message="",
                           title="Irish Energy Assets | Log In")


@app.route('/log_out')
def log_out():
    """
    Renders index.html without username set.
    """
    return redirect('/')


@app.route('/check_username', methods=['POST'])
def check_username():
    """
    Module accepts POST of username from log_in.html.
    Return filtered index.html or appropriete message on log_in.html.
    """

    if request.method == "POST":
        username = request.form["username"]
        users = read_json_data("data/users.json")
        attributes = read_json_data('static/data/json/' +
                                    'relevent_attributes.json')

        if username.lower() not in users:
            message = "That is not a valid username."
            return render_template("log_in.html",
                                    message=message,
                                    username="")
        elif username == 'admin':
            assets = sort_collection('Name', False,
                                        mongo.db.all_assets.find())
        else:
            assets = filter_collection('Company', [username],
                                        mongo.db.all_assets.find())

        return redirect(url_for('assets', username=username))


@app.route('/admin/<username>')
def admin(username):
    """
    Renders admin.html.
    """
    back_ups = os.listdir('static/data/json/backups')
    back_ups.sort(reverse=True)
    types = list_attr_values('Type', mongo.db.all_assets.find())
    counties = read_json_data('static/data/json/Irish_Counties.json')
    return render_template('admin.html',
                           username=username,
                           back_ups=back_ups,
                           types=types,
                           counties=counties,
                           title="Irish Energy Assets | Admin")

@app.route('/json_backup/<username>')
def json_backup(username):
    """
    Renders admin.html after creating local json backup of mongo database.
    """
    backup_mongo_collection(mongo.db.all_assets.find())
    back_ups = os.listdir('static/data/json/backups')
    back_ups.sort(reverse=True)
    types = list_attr_values('Type', mongo.db.all_assets.find())
    counties = read_json_data('static/data/json/Irish_Counties.json')
    return admin(username)

@app.route('/over_write_db/<username>', methods=['POST'])
def over_write_db(username):
    """
    Renders admin.html after overwriting the mongo database with local backup
    json. A local backup of the current mongo database is created before
    overwriting.
    """
    if request.method == "POST":
        json_file = request.form["backup_select"]
        local_collection =  read_json_data('static/data/json/backups/%s'
                                           % json_file)
        overwrite_with_backup(local_collection, mongo.db.all_assets)

    back_ups = os.listdir('static/data/json/backups')
    back_ups.sort(reverse=True)
    types = list_attr_values('Type', mongo.db.all_assets.find())
    counties = read_json_data('static/data/json/Irish_Counties.json')
    return admin(username)

@app.route('/add_asset/<username>', methods=['POST'])
def add_asset(username):
    """
    Renders admin.html after adding new asset to database.
    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    node_address =  "%s, %s, %s, %s, %s, %s" % (request.form['NodeAddress0'],
                                                request.form['NodeAddress1'],
                                                request.form['NodeAddress2'],
                                                request.form['NodeAddress3'],
                                                request.form['NodeAddress4'],
                                                request.form['NodeAddress5'])

    asset_doc = {"Name": request.form['Name'],
                 "Type":  request.form['Type'],
                 "SubType":  request.form['SubType'],
                 "MEC_MW":  request.form['MEC_MW'],
                 "Status":  request.form['Status'],
                 "GenRef":  request.form['GenRef'],
                 "County":  request.form['County'],
                 "Company":  request.form['Company'],
                 "NetworkType":  request.form['NetworkType'],
                 "SystemOperator":  request.form['SystemOperator'],
                 "Node":  request.form['Node'],
                 "NodeVoltage_kV":  request.form['NodeVoltage_kV'],
                 "NodeAddress":  node_address,
                 "FirstAdded": timestr}

    mongo.db.all_assets.insert_one(asset_doc)

    back_ups = os.listdir('static/data/json/backups')
    back_ups.sort(reverse=True)
    types = list_attr_values('Type', mongo.db.all_assets.find())
    counties = read_json_data('static/data/json/Irish_Counties.json')

    return admin(username)

@app.route('/edit_asset/<username>/<asset_id>')
def edit_asset(username, asset_id):
    """
    Renders edit_asset.html for editing a defined asset.
    """
    print(asset_id)
    print(username)
    assets = mongo.db.all_assets.find()
    attributes = list_attr_collection(assets)
    types = list_attr_values('Type', mongo.db.all_assets.find())
    counties = read_json_data('static/data/json/Irish_Counties.json')
    asset = mongo.db.all_assets.find_one({'_id': ObjectId(asset_id)})
    node_address = asset['NodeAddress']
    node_address_ls = list(node_address.split(","))
    return render_template('edit_asset.html',
                           types=types,
                           counties=counties,
                           attributes=attributes,
                           asset=asset,
                           node_address_ls=node_address_ls,
                           username=username,
                           title="Irish Energy Assets | Edit Asset")


@app.route('/update_asset/<username>/<asset_id>', methods=['POST'])
def update_asset(username, asset_id):
    """
    Renders index.html after updating asset edited in edit_asset.html
    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    node_address =  "%s, %s, %s, %s, %s, %s" % (request.form['NodeAddress0'],
                                                request.form['NodeAddress1'],
                                                request.form['NodeAddress2'],
                                                request.form['NodeAddress3'],
                                                request.form['NodeAddress4'],
                                                request.form['NodeAddress5'])

    mongo.db.all_assets.update(
                {'_id': ObjectId(asset_id)},
                {'$set': {
                 "Name": request.form['Name'],
                 "Type":  request.form['Type'],
                 "SubType":  request.form['SubType'],
                 "MEC_MW":  request.form['MEC_MW'],
                 "Status":  request.form['Status'],
                 "GenRef":  request.form['GenRef'],
                 "County":  request.form['County'],
                 "Company":  request.form['Company'],
                 "NetworkType":  request.form['NetworkType'],
                 "SystemOperator":  request.form['SystemOperator'],
                 "Node":  request.form['Node'],
                 "NodeVoltage_kV":  request.form['NodeVoltage_kV'],
                 "NodeAddress":  node_address,
                 "LastUpdated": timestr}})

    return redirect(url_for('assets', username=username))


@app.route('/delete_asset/<username>/<asset_id>')
def delete_asset(asset_id, username):
    """
    Renders index.html after deleting asset from database.
    """
    mongo.db.all_assets.remove({'_id': ObjectId(asset_id)})
    return redirect(url_for('assets', username=username))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
