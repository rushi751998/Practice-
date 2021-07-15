from os import close
from numpy.lib.function_base import piecewise
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
from datetime import datetime as dt

start = (dt.now())


data_frame = pd.read_csv ('D:\Pythoon\Pandas\Bhavcopy.csv') 
# print (data_frame)
symbol_list,close = data_frame["SYMBOL"], data_frame["CLOSE"]
new_close = []
for i in close :
    if i >100 and i <10000:
        new_close.append (i)
    else:
        pass
print(len (new_close))

mean = np.mean(new_close)
# print (mean)
down = (dt.now()-start)
print (down)


'''
plt.hist(new_close)
plt.xlabel ("Stock Names")
plt.ylabel ("Stock Price")
plt.title("Price Of stocks")
# plt.show()
'''