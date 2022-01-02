from flask import Flask, jsonify, request
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
    since = request.args.get('since', default = 2020, type = int)
    upto = request.args.get('upto', default = None, type = int)

    data = get_yearly(since, upto)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

    

@app.route("/yearly/<year>")
def findYearBased(year):
    data = get_year_based(year)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

        


    

if __name__ == "__main__":
    app.run()