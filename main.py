import datetime as dt
from db import connection as _conn
import requests 
import pandas as pd

import io
from math import pi
import pandas as pd
from bokeh.plotting import figure, show, output_file

import matplotlib.pyplot as plt

def send_request_api(url):

    headers = {'content-type': 'application/json; charset=utf-8'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise f'Falha na chamada da API. Erro {response.status_code}'


def get_df(url):


    dataJson = send_request_api(url)
    engine = _conn.conn_engine()
    listPeriodStart = []
    listPeriodEnd = []
    listPriceLow = []
    listPriceHigh = []
    listPriceOpen = []
    listPriceClose = []
    dataDict= {}
    dfBtc = None

    for i in range(len(dataJson)) :
        
        periodStartApi = dt.datetime.strptime(dataJson[i]['time_period_start'][:19], '%Y-%m-%dT%H:%M:%S')
        periodEndApi = dt.datetime.strptime(dataJson[i]['time_period_end'][:19], '%Y-%m-%dT%H:%M:%S')
        listPeriodStart.append(str(dt.datetime.strftime(periodStartApi, '%Y-%m-%d %H:%M:%S')))
        listPeriodEnd.append(str(dt.datetime.strftime(periodEndApi, '%Y-%m-%d %H:%M:%S')))
        listPriceLow.append(float(dataJson[i]['price_low']))
        listPriceHigh.append(float(dataJson[i]['price_high']))
        listPriceOpen.append(float(dataJson[i]['price_open']))
        listPriceClose.append(float(dataJson[i]['price_close']))

    dfBtc = pd.DataFrame({'PriceOpen':  listPriceOpen,
     'PriceHigh': listPriceHigh,
     'PriceLow': listPriceLow,
     'PriceClose': listPriceClose,
     'PeriodStart': listPeriodStart,
     'PeriodEnd': listPeriodEnd})

    dfBtc.to_sql('BitCoin', con=engine, if_exists='replace', index=False)
    print("Inserção no banco de dados concluída !")
    
    return dfBtc

def graphic_thirty_days(url):
    dfBtc = get_df(url)
    print(dfBtc)
    dfBtc["PeriodEnd"] = pd.to_datetime(dfBtc["PeriodEnd"])
    dfBtc["PeriodStart"] = pd.to_datetime(dfBtc["PeriodStart"])

    inc = dfBtc.PriceClose > dfBtc.PriceOpen
    dec = dfBtc.PriceOpen > dfBtc.PriceClose
    w = 12*60*60*1000

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    p = figure(
        x_axis_type="datetime", 
        tools=TOOLS, 
        plot_width=1000,
        sizing_mode="stretch_width",
        height=250,

        title = "Visão Bitcoin 30 dias")
    p.xaxis.major_label_orientation = pi/4
    p.grid.grid_line_alpha=0.5

    p.segment(dfBtc.PeriodStart, dfBtc.PriceHigh, dfBtc.PeriodStart, dfBtc.PriceLow,  color="black")

    p.vbar(dfBtc.PeriodStart[inc], w, dfBtc.PriceOpen[inc], dfBtc.PriceClose[inc], fill_color="#D5E1DD", line_color="black")

    p.vbar(dfBtc.PeriodStart[dec], w, dfBtc.PriceOpen[dec], dfBtc.PriceClose[dec], fill_color="#F2583E", line_color="black")


    output_file("btcCandlestick.html", title="Visão Bitcoin 30 dias")

    show(p)


def graphic_five_years(url):
    dfBtc = get_df(url)
    print(dfBtc)
    plt.title('Bitcoin em 5 anos')
    plt.plot(pd.to_datetime(dfBtc['PeriodEnd']).dt.strftime('%Y'), dfBtc['PriceClose'])
    plt.xticks(rotation=30, ha='right')
    
    # Giving x and y label to the graph
    plt.xlabel('Anos')
    plt.ylabel('Preço fechado')
    plt.show()


















