from datetime import date, datetime
from dateutil.parser import parse
import requests

baseUrl = "https://data.covid19.go.id/public/api/update.json"

def get_general():
    fetch = requests.get(baseUrl)
    res = fetch.json()["update"]["total"]
    res2 = fetch.json()["update"]["penambahan"]
    result = {
        "total_positive": res["jumlah_positif"],
        "total_recovered": res["jumlah_sembuh"],
        "total_deaths": res["jumlah_meninggal"],
        "total_active": res["jumlah_dirawat"],
        "new_positive": res2["jumlah_positif"],
        "new_recovered": res2["jumlah_sembuh"],
        "new_deaths": res2["jumlah_meninggal"],
        "new_active": res2["jumlah_dirawat"],
    }
    
    return result

def get_yearly(since, upto = None):
    fetch = requests.get(baseUrl)
    r = fetch.json()
    harian = r["update"]["harian"]

    totalresults = []

    if upto == None:
        upto = datetime.today().year

    i = 0
    while i < len(harian):
        data = harian[i]
        year = parse(str(data["key_as_string"])).year

        if since <= year and year <= upto:
            result = {
                "year": year,
                "positive": 0,
                "recovered": 0,
                "deaths": 0,
                "active": 0,
            }

            pointedYear = year

            while pointedYear == year and i < len(harian):
                result["positive"] += data["jumlah_positif"]["value"]
                result["recovered"] += data["jumlah_sembuh"]["value"]
                result["deaths"] += data["jumlah_meninggal"]["value"]
                result["active"] += data["jumlah_dirawat"]["value"]
            
                i += 1

                if i < len(harian):
                    data = harian[i]
                    pointedYear = parse(str(data["key_as_string"])).year
                
            totalresults.append(result)
        else:
            i += 1

    return totalresults

def get_year_based(year):
    fetch = requests.get(baseUrl)
    r = fetch.json()
    harian = r["update"]["harian"]

    result = {
        "year": year,
        "positive": 0,
        "recovered": 0,
        "deaths": 0,
        "active": 0,
    }

    for i in harian:
        pointedYear = parse(str(i["key_as_string"])).year

        if pointedYear == int(year):
            result["positive"] += i["jumlah_positif"]["value"]
            result["recovered"] += i["jumlah_sembuh"]["value"]
            result["deaths"] += i["jumlah_meninggal"]["value"]
            result["active"] += i["jumlah_dirawat"]["value"]

        if pointedYear > int(year):
            return result
    return result

def get_monthly_based(year, month):
    fetch = requests.get(baseUrl)
    r = fetch.json()
    harian = r["update"]["harian"]

    result = {
        "month": "{}-{}".format(year, month),
        "positive": 0,
        "recovered": 0,
        "deaths": 0,
        "active": 0,
    }

    for i in harian:
        pointedMonth = parse(str(i["key_as_string"]))

        if pointedMonth.year == int(year) and pointedMonth.month == int(month):
            result["positive"] += i["jumlah_positif"]["value"]
            result["recovered"] += i["jumlah_sembuh"]["value"]
            result["deaths"] += i["jumlah_meninggal"]["value"]
            result["active"] += i["jumlah_dirawat"]["value"]
            return result


    return result

def get_daily_based(year, month, day):
    fetch = requests.get(baseUrl)
    r = fetch.json()
    harian = r["update"]["harian"]

    result = {
        "date": "",
        "positive": 0,
        "recovered": 0,
        "deaths": 0,
        "active": 0,
    }

    for i in harian:
        pointedDay = parse(str(i["key_as_string"]))

        if pointedDay.year == int(year) and pointedDay.month == int(month) and pointedDay.day == int(day):
            result["date"] += str(pointedDay.date())
            result["positive"] += i["jumlah_positif"]["value"]
            result["recovered"] += i["jumlah_sembuh"]["value"]
            result["deaths"] += i["jumlah_meninggal"]["value"]
            result["active"] += i["jumlah_dirawat"]["value"]
            return result


    return result
        
# print(get_yearly(2020))