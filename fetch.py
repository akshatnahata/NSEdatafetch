from nsepy import get_history
from datetime import date

data = get_history(symbol="SBIN", start=date(2020,1,1), end=date(2021,1,31))
print(data[['Close']])
