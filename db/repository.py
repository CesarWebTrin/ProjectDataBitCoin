def insert_format():

    dataJson = send_request_api()
    engine = conn_engine()
    listPeriodStart = []
    listPeriodEnd = []
    listPriceLow = []
    listPriceHigh = []
    listPriceOpen = []
    listPriceClose = []
    dataDict= {}
    dfBtc = None

    for i in range(len(dataJson)) :
        
        periodStartApi = datetime.strptime(dataJson[i]['time_period_start'][:19], '%Y-%m-%dT%H:%M:%S')
        periodEndApi = datetime.strptime(dataJson[i]['time_period_end'][:19], '%Y-%m-%dT%H:%M:%S')
        listPeriodStart.append(str(datetime.strftime(periodStartApi, '%Y-%m-%d %H:%M:%S')))
        listPeriodEnd.append(str(datetime.strftime(periodEndApi, '%Y-%m-%d %H:%M:%S')))
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

    dfBtc.to_sql('BitCoin', con=engine, if_exists='append', index=False)

