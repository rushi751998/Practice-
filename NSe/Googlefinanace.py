

from nsepy import get_history
from datetime import datetime
import dateutil.relativedelta
import matplotlib.pyplot as plt
'''
symbol = str (input ("Ener Name : "))

End_Date = int(input(" End Date : ")
'''

'''
plt.style.use('fivethirtyeight')
to_date=datetime.now()
to_date=datetime.strftime(to_date,'%Y,%m,%d')
to_date=datetime.strptime(to_date,'%Y,%m,%d')
from_date=to_date-dateutil.relativedelta.relativedelta(month=1)
data=get_history(symbol='RELIANCE',start=from_date,end=to_date)
print(data)
data['Close'].plot()
plt.show()
'''
from nsepy import get_history as gh
import datetime as dt
import dateutil.relativedelta as dr
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
tradingsymbol='NIFTY BANK'
end=dt.date.today()
start=end-dr.relativedelta(days=30)
data=gh(tradingsymbol,start,end,index=True)
data['High'].plot()
plt.show()