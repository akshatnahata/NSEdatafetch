import nsepy
import time
import pprint
from datetime import date
import concurrent.futures
import pandas as pd
import os
from nsepy import get_history
# nifty_opt = get_history(symbol="BANKNIFTY",start=date(2021,8,13),end=date(2021,8,18),index=True,option_type='CE',strike_price=36000,expiry_date=date(2021,8,18))
Volume = 0
while(True):
    # Volume = float(nsepy.get_quote("BANKNIFTY",instrument="FUTIDX",expiry=date(2021,9,30),)["data"][0]["changeinOpenInterest"].replace(",",""))
    diff = float(nsepy.get_quote("BANKNIFTY",instrument="FUTIDX",expiry=date(2021,9,30),)["data"][0]["numberOfContractsTraded"].replace(",",""))-Volume
    print(diff*25)
    if(diff>50000):
        os.system('say "Banknifty volume greater"')

    Volume = float(nsepy.get_quote("BANKNIFTY",instrument="FUTIDX",expiry=date(2021,9,30),)["data"][0]["numberOfContractsTraded"].replace(",",""))
    time.sleep(180)
