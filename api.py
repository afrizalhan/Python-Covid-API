from flask import Flask, jsonify
import requests
from handler import *


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/", methods = ["GET"])
def findGeneral():
    data = get_general()
    
    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

@app.route("/yearly/", methods = ["GET"])
def findYearly():
    since = requests.args.get('since', default= 2020)
    upto = requests.args.get('upto', default= None)

    

# @app.route("/yearly/<year>")
# def findYearBased(year):

        


    

if __name__ == "__main__":
    app.run()