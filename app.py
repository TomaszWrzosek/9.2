import requests
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
data1 = response.json()

data2 = data1[0]

rates = data2["rates"]

csv_file = "rates1.csv"

rates_map = {}

with open('rates1.csv', 'w', newline='') as csvfile:
    fieldnames = ['currency','code','bid','ask']
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)

    writer.writeheader()
    for rate in rates:
        writer.writerow(rate)
        code = rate['code']
        rates_map[code] = rate
        
to_bid = rates_map['USD']  
bid = to_bid['bid']

@app.route("/calculate/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        data = request.values
        value = data.get('value')
        currency = data.get('currency')
        get_currency = rates_map[currency]
        the_bid = get_currency['bid']
        calculate = int(value)*the_bid
       
        print(calculate)
        print(the_bid)
        
        return render_template("calc.html", calculate=calculate)
       
  
    return render_template("calc.html")

if __name__ == "__main__":
    app.run(debug=True)