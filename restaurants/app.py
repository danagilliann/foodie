import json

from flask import Flask
from flask import render_template
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'restaurantinspection'
COLLECTION_NAME = 'restaurants'
FIELDS = {'DBA':True, 'BORO': True, 'BUILDING':True, 'STREET':True, 'ZIPCODE':True, 'GRADE':True, 'INSPECTION DATE':True, '_id': False}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restaurantinspection/restaurants")
def restaurantinspection_restaurants():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    restaurants = collection.find(projection=FIELDS)
    json_restaurants = []
    for restaurant in restaurants:
        json_restaurants.append(restaurant)
    json_restaurants = json.dumps(json_restaurants, default=json_util.default)
    connection.close()
    return json_restaurants

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
