from datetime import date
import concurrent.futures
import pandas as pd
import os
from nsepy import get_history
import nsepy
import pprint

diff = nsepy.get_quote("BANKNIFTY",instrument="FUTIDX",expiry=date(2021,9,30),)["data"]
pprint.pprint(diff)