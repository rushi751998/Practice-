import nsetools
from  nsetools import Nse
import pandas as pd
import numpy as np
nse = Nse()
# print(nse)
import pprint
from pprint import pprint
q = nse.get_stock_codes()
pprint(q)
# df = pd.DataFrame(q,index="Head")
# print(df)
# q.to_csv("Stock Codes",index = False)
