from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
import travel_scrape

#make an app instance
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

'''Define the Routes'''

#index
@app.route('/')
def home():
    travel = mongo.db.travel.find_one()
    return render_template('index.html', travel=travel)

@app.route('/scrape')
def scraper():
    travel = mongo.db.travel
    travel_data = travel_scrape.scrape()
    print(travel_data)
    travel.update({}, travel_data, upsert=True)
    print("saved!")
    return redirect("/", code=302)

#run the app
if __name__ == '__main__':
    app.run(debug=True)