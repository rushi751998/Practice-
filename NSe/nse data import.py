from datetime import date
from nsepy import get_history
import matplotlib as plt
import pandas as pd

'''

nifty_opt = get_history(symbol="BANKNIFTY",
                        start=date(2021,4,25),
                        end=date(2021,5,6),
                        index=True,
                        option_type=('CE'),
                        strike_price=34000,
                        expiry_date=date(2021,5,6))
                         
print(nifty_opt)
'''

nifty_ = get_history(symbol="BANKNIFTY",
                        start=date(2021,4,25),
                        end=date(2021,5,6),
                        index=True,
                        option_type=('PE'),
                        strike_price=34000,
                        expiry_date=date(2021,5,6))

print(nifty_)