import nsepy
import time
import pprint
import concurrent.futures
import pandas as pd
import os

symbols = ["reliance","tatamotors","tatasteel","grasim"]
def data(symbol):
    data_live = {}
    data_nse = nsepy.get_quote(symbol.upper().replace("&","%26%"))["data"][0]
    # Low = float(nsepy.get_quote(symbol)["data"][0]["dayLow"].replace(",",""))
    # Volume = float(nsepy.get_quote(symbol)["data"][0]["totalTradedVolume"].replace(",",""))
    # Vwap = float(nsepy.get_quote(symbol)["data"][0]["averagePrice"].replace(",",""))
    # Ltp = float(nsepy.get_quote(symbol)["data"][0]["lastPrice"].replace(",",""))
    data_live[symbol.upper()] = {"Open":float(data_nse["open"].replace(",","")),
    "High":float(data_nse["dayHigh"].replace(",","")),
    "Low":float(data_nse["dayLow"].replace(",","")),
    "Volume":float(data_nse["totalTradedVolume"].replace(",","")),
    "Vwap":float(data_nse["averagePrice"].replace(",","")),
    "Ltp":float(data_nse["lastPrice"].replace(",",""))}
    # pprint.pprint(nsepy.get_quote(symbol))
    # data_nse = nsepy.get_quote(symbol)["data"][0]["lastPrice"].replace(",","")
    # data_nse = data_nse["data"][0]["lastPrice"]
    # data_nse = data_nse.replace(",","")
    # data_nse = float(data_nse)
    # pprint.pprint(data_live)
    return (data_live)
# for i in symbols:
#     print(data(i))    
def get_multiple_stocks_data(symbol_list):
    multiple_stocks = {}
    # for i in symbol_list:
    #     single_stock = data(i)
    #     for k,v in single_stock.items():
    #         multiple_stocks[k]=v
    with concurrent.futures.ThreadPoolExecutor() as executer:
        results = executer.map(data,symbol_list)
        for i in results:
            for k,v in i.items():
                multiple_stocks[k] = v

    return(multiple_stocks)       


# start = time.perf_counter()
previousVol = 0
while True:
    stocks_data = (get_multiple_stocks_data(symbols))
    
    print((stocks_data["GRASIM"]["Volume"])-previousVol)
    if((stocks_data["GRASIM"]["Volume"]-previousVol)>200):
        os.system('say "Grasim Volume greater than 200"')

    previousVol = ((stocks_data["GRASIM"]["Volume"]))
    time.sleep(180)

# df = pd.DataFrame(stocks_data).transpose()
# print(df)
# stop = time.perf_counter()
# print(stop-start)
