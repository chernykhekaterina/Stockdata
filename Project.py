from flask import Flask, render_template, request

import pandas as pd

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import sys


app = Flask("Final_Project")
app.debug = True

@app.route("/numbers", methods=["POST"])
def stockchart():

    print "inside stockchart"
    symbol = request.form.get("symbol")
    print symbol

    ts = TimeSeries(key='GJUITI4Y9S0JG9D3', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1min', outputsize='full')
    print data
    print data.to_html(formatters={'Name': lambda x: '<b>' + x + '</b>'})
    return render_template("stockdata.html", stockdata=data, symbol=symbol)




@app.route("/")
def dropdown():
    symbol_list = ["GOOGL","MSFT","IBM", "AAPL"]
    return render_template("index.html", symbol_list=symbol_list)


if __name__ == "__main__":
    app.run()
