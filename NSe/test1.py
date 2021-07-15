from datetime import date
from nsepy import get_history
import matplotlib as plt
import pandas as pd

'''Study.py'''

'''
nifty_opt = get_history(symbol="BANKNIFTY",
                        start=date(2021,4,25),
                        end=date(2021,5,6),
                        index=True,
                        option_type=('CE'),
                        strike_price=34000,
                        expiry_date=date(2021,5,6))

'''
# print(nifty_opt)

# aa = get_history(symbol="NIFTY",start=date(2021,4, 1), end=date(2021,4,29),futures=True,expiry_date=date(2021, 4, 29))
a= date(2021,5,1)
b =date(2021,5,7)

stock_fut = get_history(symbol="BANKNIFTY",
                            start=a,
                            end=b,
                            futures=True,
                            index = True,
                            expiry_date=date(2021, 5, 27))

# print(stock_fut)
c=stock_fut["Expiry"]

print (c)

d = stock_fut["High"]

# e = f"{c}+{d}"
# print(e)

# d =stock_fut['Symbol']

# e =[c+d]
# print(e)

# rushi = pd.DataFrame(stock_fut)
# # print(d)


'''

stock_futa = get_history(symbol="NIFTY",
                            start=a,
                            end=b,
                            futures=True,
                            index = True,
                            expiry_date=date(2021, 5, 27))
tca = pd.DataFrame(stock_futa)


# print(tc)
# print(tca)

tc =tc.astype(str)
tca =tca.astype(str)
data = tc




# print(ap)






ds= ap.to_csv("Rushikesh2.csv")
print(ds)
'''