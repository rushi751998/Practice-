from datetime import date
from nsepy import get_history
import matplotlib as plt
import pandas as pd
'''
sbin = get_history(symbol='SBIN',start=date(2015,1,1),end=date(2015,1,5))
IOC = get_history(symbol='IOC',start=date(2015,1,1),end=date(2015,1,5))
# print( sbin)
# print( IOC )
a = ( IOC + sbin)
print( a)
'''


stock_fut = get_history(symbol="Nifty",
                            start=date(2021,4,20),
                            end=date(2021,5,5),
                            futures=True,
                            index = True,
                            expiry_date=date(2021,5,27))
# print(stock_fut)

va = pd.DataFrame(stock_fut)
# va.to_csv('Sample3.csv',index = True)
print(va.head(2))

'''
stock_opt = get_history(symbol="SBIN",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        option_type="CE",
                        strike_price=300,
                        expiry_date=date(2015,1,29))
                        
print((stock_opt))


nifty_fut = get_history(symbol="NIFTY",
                        start=date(2015,1,1),
                        end=date(2015,1,10),
                        index=True,
                        futures=True,
                        expiry_date=date(2015,1,29))
print((nifty_fut))


nifty_opt = get_history(symbol="NIFTY",
                        start=date(2021,4,25),
                        end=date(2021,5,6),
                        index=True,
                        option_type='CE',
                        strike_price=14650,
                        expiry_date=date(2021,5,6))




ca=pd.DataFrame(nifty_opt)
a= ca.to_csv
print(a)
# print((nifty_opt))



vix = get_history(symbol="INDIAVIX",
            start=date(2015,1,1),
            end=date(2015,1,10),
            index=True)


print((vix))



#feetch expiry dates



from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2015, month=1)
# print(expiry)

from nsepy.derivatives import get_expiry_date
expiry = get_expiry_date(year=2015, month=1)
stock_opt = get_history(symbol="SBIN",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            futures=True,
                            expiry_date=get_expiry_date(2015,1))
print((stock_opt))


# Index P/E ratio history
from nsepy import get_index_pe_history
nifty_pe = get_index_pe_history(symbol="NIFTY",
                                start=date(2015,1,1),
                                end=date(2015,1,10))
print(nifty_pe)

'''