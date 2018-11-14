import os
import tabula
import json
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from geopy.geocoders import Nominatim
import time



app = Flask(__name__)
with open('db_details.txt', 'r') as f:
    db_details = f.readlines()
    app.config["MONGO_DBNAME"] = db_details[0]
    app.config["MONGO_URI"] = db_details[1]

mongo = PyMongo(app)

def convert_pdf_to_csv(pdf_file):
    """
    Converts pdf file into csv and stores in same directory
    """
    tabula.convert_into(pdf_file, 
                        str(pdf_file[:-4] + ".csv"),
                        output_format="csv",
                        spreadsheet=True,
                        pages='all')


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
        
def update_collection_with_attr(attr, value, collection):
    """
    Used to update collecction if attr does not exist with attr = value.
    """
    for doc in collection:
        if attr not in doc:
            doc[attr] = value
    return collection

def update_all_asset_json():
    """
    Iterates through directory static/data/json and combines all json files
    into single file.
    """
    all_assets = []
    for file in os.listdir("static/data/json"):
        if file != "ireland_energy_assets_connected&contracted.json":
            file_path = "static/data/json/%s" % file
            data = read_json_data(file_path)
            for asset in data:
                all_assets.append(asset)
    write_json_data(all_assets, "static/data/json/" /
                    + "ireland_energy_assets_connected&contracted.json")

def bulk_insert_assets(local_collection, mongo_collection):
    """
    Deletes entire mongo_collection and then fills it with local_collection.
    """
    result = mongo.db.all_assets.delete_many({ })
    for doc in local_collection:
        mongo_collection.insert_one(doc)

def my_autopct(pct):
    """
    Used for changing how percentage is displayed in matplotlip pie chart.
    """
    return ('%0.1f%%' % pct) if pct > 0 else ''

def get_node_address():
    """
    Uses geopy to assign the NodeAddress. 
    Prints out list of Nodes not found and _id's with no node attribute.
    """
    not_found = []
    no_node = []
    all_assets = mongo.db.all_assets.find()
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    for asset in all_assets:
        min_delay_seconds = 2
        if 'Node' in asset and 'NodeAddress' not in asset:
            node_location = asset['Node'] + " Ireland"
            location = geolocator.geocode(node_location)
            if hasattr(location, 'address'):
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                    {"$set": {"NodeAddress" : location.address}}, upsert=True)
            else:
                not_found.append(asset['Node'])
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                     {"$set": {"NodeAddress" : "NA"}})
        else:
            no_node.append(asset["_id"])

def get_asset_address():
    """
    Uses geopy to assign the NodeAddress. 
    Prints out list of Nodes not found and _id's with no node attribute.
    """
    not_found = []
    no_node = []
    all_assets = mongo.db.all_assets.find()
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    for asset in all_assets:
        min_delay_seconds = 2
        if 'Name' in asset:
            asset_location = asset['Name'] + " Ireland"
            location = geolocator.geocode(asset_location)
            if hasattr(location, 'address'):
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                   {"$set": {"AssetAddress" : location.address}}, upsert=True)
            else:
                not_found.append(asset['Name'])
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                   {"$set": {"AssetAddress" : "NA"}})
            if hasattr(location, 'latitude') and hasattr(location, 'longitude'):
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                   {"$set": {"AssetLatitude" : location.latitude}}, upsert=True)
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                  {"$set": {"AssetLatitude" : location.longitude}}, upsert=True)
            else:
                not_found.append(asset['Name'])
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                   {"$set": {"AssetLatitude" : "NA"}}, upsert=True)
                mongo.db.all_assets.update_one({'_id': asset['_id']},
                   {"$set": {"AssetLatitude" : "NA"}}, upsert=True)

        else:
            no_node.append(asset["_id"])

def update_node_address():
    """
    Used to add addresses of the nodes not found by geopy.
    """
    nodes = ['Drybridge',
            'Screeb',
            'Portlaoise',
            'Cathaleens Fall',
            'Boggeragh',
            'Reamore',
            'Barnahealy',
            'Barnadivine',
            'Oweninney',
            'Longpoint',
            "Cathaleen's Fall",
            'Blundlestown']

    node_address_list = [
        'Drybridge,Tullyallen, Drogheda, County Louth, Ireland', 
        'Screeb, Salthill, County Galway, Ireland', 
        'Portlaoise, County Laois, Leinster, Ireland', 
        'Cathaleens Fall, Beleek Road, Tully, Ballyshannon, County Donegal, Ireland', 
        'Boggeragh, County Cork, Ireland',
        'Reamore, County Kerry, Ireland', 
        'Barnahealy, Ringaskiddy , County Cork, Ireland', 
        'Barnadivine, County Cork, Ireland', 
        'Oweninney, Moneynierin, County Mayo, Ireland', 
        'Longpoint, County Cork, Ireland', 
        "Cathaleens Fall, Beleek Road, Tully, Ballyshannon, County Donegal, Ireland", 
        'Blundlestown, Polleban, County Meath, Ireland']

    for asset in mongo.db.all_assets.find():
        if 'Node' in asset and asset['Node'] in nodes:
            index = nodes.index(asset['Node'])
            node_address = node_address_list[index]
            mongo.db.all_assets.update_one({'_id': asset['_id']},
                 {"$set": {"NodeAddress" : node_address}}, upsert=True)

def company_pie():
    """
    Used to generate .svg pie chart showing capacity share of companies
    """
    companies = list_attr_values("Company", mongo.db.all_assets.find())
    companies_tot_mw = []
    company_tot_mw = 0
    all_assets = mongo.db.all_assets.find()
    total = 0
    for asset in all_assets:
        if 'Company' in asset and asset['Company'] != "":
            total += asset['MEC_MW']
    for company in companies:
        all_assets = mongo.db.all_assets.find()
        company_tot_mw = 0
        for asset in all_assets:
            if 'Company' in asset and str(asset['Company']) == company:
                    company_tot_mw += asset['MEC_MW']
        companies_tot_mw.append(company_tot_mw)
    
    companies = [x for _,x in sorted(zip(companies_tot_mw, companies), \
                                      reverse=True)]
    companies_tot_mw = sorted(companies_tot_mw, reverse=True)
    other_tot_mw = 0

    for mw in reversed(companies_tot_mw):
        index = companies_tot_mw.index(mw)
        if mw/total <= 0.02:
            other_tot_mw += mw
            del companies_tot_mw[index]
            del companies[index]
    if other_tot_mw > 0:
        companies.append('Other')
        companies_tot_mw.append(other_tot_mw)

    for company in companies:
        index = companies.index(company)
        company_percentage = \
            round((companies_tot_mw[index]*100/total), 1)
        companies[index] = companies[index] + " - " + \
            str(company_percentage) + "%"
 
    fig1, ax1 = plt.subplots()

    texts, autotexts = ax1.pie(companies_tot_mw,
                               labels=companies,
                               startangle=90,
                               labeldistance=1,
                               rotatelabels=True)
    ax1.set_title("Company share of Assets", pad=60, color='white')
     
    for autotext in autotexts:
        autotext.set_color('white')
    ax1.axis('equal')
    fig1.tight_layout()
    fig1.set_facecolor('black')
    fig1.savefig('static/company.svg', transparent=True)


def county_pie():
     """
     Used to generate .svg pie chart showing capacity share of counties.
     """
     counties = read_json_data("static\data\json\Irish_Counties.json")
     counties_tot_mw = []
     county_tot_mw = 0
     all_assets = mongo.db.all_assets.find()
     total = 0
     for asset in all_assets:
         if asset['Status'] != 'Contracted':
             total += asset['MEC_MW']
     for county in counties:
         all_assets = mongo.db.all_assets.find()
         county_tot_mw = 0
         for asset in all_assets:
             if "NodeAddress" in asset and county in asset["NodeAddress"] \
                 and  asset["Status"] != 'Contracted':
                     county_tot_mw += asset['MEC_MW']
         counties_tot_mw.append(county_tot_mw)
    
     counties = [x for _,x in sorted(zip(counties_tot_mw, counties),
                                     reverse=True)]
     counties_tot_mw = sorted(counties_tot_mw, reverse=True)
     other_tot_mw = 0

     for mw in reversed(counties_tot_mw):
         index = counties_tot_mw.index(mw)
         if mw/total <= 0.02:
             other_tot_mw += mw
             del counties_tot_mw[index]
             del counties[index]
     if other_tot_mw > 0:
         counties.append('Other')
         counties_tot_mw.append(other_tot_mw)

     for county in counties:
         index = counties.index(county)
         county_percentage = round((counties_tot_mw[index]*100/total), 1)
         counties[index] = counties[index] + " - " + \
                           str(county_percentage) + "%"
 
     fig1, ax1 = plt.subplots()

     texts, autotexts = ax1.pie(counties_tot_mw,
                                labels=counties,
                                startangle=90,
                                labeldistance=1,
                                rotatelabels=True)
     ax1.set_title("county share of Assets", pad=60, color='white')
     
     for autotext in autotexts:
         autotext.set_color('white')
     ax1.axis('equal')
     fig1.tight_layout()
     fig1.set_facecolor('black')
     fig1.savefig('static/county.svg', transparent=True)

def assign_county():
    counties = read_json_data("static/data/json/Irish_Counties.json")
    node_address = 0
    just_county = 0
    neither = 0
    for doc in mongo.db.all_assets.find():
        for county in counties:
            county_full = "County %s" % county
            if 'NodeAddress' in doc and county_full in doc['NodeAddress']:

                mongo.db.all_assets.update_one({'_id': doc['_id']},
                                                {"$set": {"County" : county}})
            elif 'County' in doc and county == doc['County']:
                just_county += 1
            else:
                neither += 1

    print(node_address)
    print(just_county)
    print(neither)

def assign_NA_to_none_nodes():
    """
    Used to set county to NA if attribute county is not in document
    or county=""
    """
    for doc in mongo.db.all_assets.find():
        if 'County' not in doc or doc['County'] == "":
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"County" : 'NA'}}, upsert=True)

def bulk_updating_systemop():
    """
    For updating all SystemOperator Attributes
    """
    timestr = time.strftime("%Y%m%d-%H%M%S")
    for doc in mongo.db.all_assets.find():
        if doc['SystemOperator'] == 'DSO':
             mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"SystemOperator" : 'ESB Networks', "NetworkType": 'Distribution', 'FirstAdded': timestr, 'LastUpdated' : timestr}}, upsert=True)
        elif doc['SystemOperator'] == 'TSO':
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"SystemOperator" : 'EirGrid', "NetworkType": 'Transmission', 'FirstAdded': timestr, 'LastUpdated' : timestr}}, upsert=True)

def updatetypes():
    """
    Update Types into sub types.
    """
    for doc in mongo.db.all_assets.find():
        if doc['Type'] == 'Natural Gas':
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"Type" : 'Nat. Gas'}}, upsert=True)
        elif doc['Type'] == 'LFG':
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"Type" : 'Biogas', "TypeSub": 'Land Fill Gas'}}, upsert=True)
        elif doc['Type'] == 'Gas' or doc['Type'] == 'Nat. Gas':
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"Type" : 'Natural Gas'}}, upsert=True)
        elif doc['Type'] == 'Water':
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"Type" : 'Hydro'}}, upsert=True)

def title_nodes():
    """
    Title-ise all node names
    """
    for doc in mongo.db.all_assets.find():
        new_node = doc['Node'].title()
        mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"Node" : new_node}}, upsert=True)

def change_keyname():
    """
    Change the key name of dictionary
    """
    for doc in mongo.db.all_assets.find():
        if 'Voltage_kV' in doc:
            NodeVoltage = doc['Voltage_kV']
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$set": {"NodeVoltage_kV" : NodeVoltage}}, upsert=True)
            mongo.db.all_assets.update_one({'_id': doc['_id']},
                {"$unset": {'Voltage_kV' : ""}})
            
def testingprint():
    address = "Bellacorick, \n Glenco ED, \n West Mayo, \n County Mayo, \n Connacht, \n Ireland"
    print(address)

testingprint()