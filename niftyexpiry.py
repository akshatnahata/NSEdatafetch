import nsepy
import time
import pprint
from datetime import date
import concurrent.futures
import pandas as pd
from nsepy import get_history
nifty_opt = get_history(symbol="BANKNIFTY",start=date(2021,8,13),end=date(2021,8,18),index=True,option_type='CE',strike_price=36000,expiry_date=date(2021,8,18))
x = pd.DataFrame(nifty_opt)
x.to_csv('expiry.csv')
