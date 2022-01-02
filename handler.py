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
    harian = fetch.json()["update"]["harian"]

    totalresults = []

    if upto == None:
        datetime.today().year

    for i in harian:
        data = harian[i]
        year = parse()