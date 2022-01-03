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

@app.route("/monthly/", methods = ["GET"])
def findMonthly():
    since = request.args.get('since', default = '2020.03', type = str)
    upto = request.args.get('upto', default = None, type = str)

    data = get_monthly(since, upto)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

@app.route("/monthly/<year>", methods = ["GET"])
def findMonthlyYearBased(year):
    since = request.args.get('since', default = '2020.03', type = str)
    upto = request.args.get('upto', default = None, type = str)

    data = get_monthly_year_based(year, since, upto)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

@app.route("/monthly/<year>/<month>")
def findMonthBased(year, month):
    data = get_monthly_based(year, month)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

@app.route("/daily/", methods = ["GET"])
def findDaily():
    since = request.args.get('since', default = '2020.03.02', type = str)
    upto = request.args.get('upto', default = None, type = str)

    data = get_daily(since, upto)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

@app.route("/daily/<year>/", methods = ["GET"])
def findDailyYearBased(year):
    since = request.args.get('since', default = '2020.03.02', type = str)
    upto = request.args.get('upto', default = None, type = str)

    data = get_daily_year_based(year, since, upto)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

@app.route("/daily/<year>/<month>/<day>")
def findDailyBased(year, month, day):
    data = get_daily_based(year, month, day)

    response = {
        "ok": True,
        "data": data,
        "message": "Data retrieved successfully",
    }
    return jsonify(response)

        


    

if __name__ == "__main__":
    app.run()