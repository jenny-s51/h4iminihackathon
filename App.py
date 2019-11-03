# import modules

from flask import Flask, render_template, request
# from flask_pymongo import PyMongo
# initialize database


# create your routes here
app = Flask(__name__)

@app.route("/", methods = ["GET"]) 

def display_home(): 
    return render_template('home.html') 

@app.route("/login", methods = ["GET"]) 

def display_login():
    return render_template('login.html')

# initializes app

# app.config["MONGO_URI"] = "mongodb://localhost:27017/socialMedia"
# mongo = PyMongo(app)
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=4000, debug=True)
