import sys
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")

@app.route("/")
def home():
    mars = mongo.db.collection.find_one()
    #print(mars)
    return render_template("index.html", mars = mars)


@app.route('/scrape')
def scrape():
   # db.collection.remove()
    mars = scrape_mars.scrape()
    mongo.db.collection.update({}, mars, upsert=True)
    return "News_title, News_snippet, Featured image , Mars_wetaher , hemisphere deatils are scrapped from Mars url"

if __name__ == "__main__":
    app.run(debug=True)