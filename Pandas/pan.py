"""import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df=pd.DataFrame({"Day":[1,2,3,4,5,6],"Visitor":[1000,2000,400,700,3000,400],"Bounce_Rate":[20,25,45,60,10,35]})
df=df.rename(columns ={"Visitor":"Users"})
print(df)

 
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
market = pd.read_csv('C:\\Users\\Vision\\OneDrive\\Desktop\\123.csv',index_col=1)

#df = market.head()
#print (df)

#df = df.set_index(['country Name'])
#print (df)


sd = market .reindex(columns=['2010','2011'])

#print(sd)

db = sd.diff(axis=1)
db.plot(kind ='bar')
plt.show()

#print(df)


