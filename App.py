# import modules

from flask import Flask, render_template, request
# from flask_pymongo import PyMongo
# initialize database

app = Flask(__name__)
# create your routes here

@app.route("/", methods = ["GET"])

def display(): 
    return render_template('home.html')

@app.route("/login", methods = ["GET"])

def displayLogin():
    return render_template('login.html')

@app.route("/signup", methods = ["GET"])

def displaySignup():
    return render_template('signup.html')

@app.route("/test", methods = ["GET"])

def displayTest():
    return render_template('test.html')

# initializes app


# app.config["MONGO_URI"] = "mongodb://localhost:27017/socialMedia"
# mongo = PyMongo(app)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)

