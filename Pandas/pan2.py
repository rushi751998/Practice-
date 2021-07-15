import pandas as pd
import numpy as np


'''
df = pd.DataFrame([1,2,3,4,5,np.nan,8,9,0])
print (df)
'''

d = pd.date_range ('20200329',periods=10)
#print(d)


#df = pd. DataFrame(np.random.randn(10,4),index =d,columns = ['a','b','c','d'])
#print (df)


df1 = pd.DataFrame({'A':[1,2,3,4],'B':pd.Timestamp ('20200321')}) 
#print (df.tail())
#print  (df1.dtypes)

print (df1.sort_index(axis=1 , ascending=False ))
