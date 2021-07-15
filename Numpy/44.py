
"""

import numpy as np
import time
import sys
size = 1000000

l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()

result = [(x,y) for x,y in zip(l1,l2)]

print((time.time()-start)*1000)

start = time.time()
    
result = a1+a2

print((time.time()-start)*1000)
"""
"""
import numpy as np
a = np.array([(10,2,3,4),(5,6,7,8)])
b = np.array([(10,2,3,4),(5,6,7,8)])
"""
#print (np.sum(a))
#print(a.sum(axis=1))
#print(np.sqrt(a))
#print(np.std (a))
#print(a/b)

#print(np.hstack((a,b)))

import numpy as np
import matplotlib.pyplot as plt
x= np.arange(0,5*np.pi,0.1)
y= np.tan(x)
plt.plot(x,y)
plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt

ar= np.array([1,2,3])
print(np.log10(ar))
"""


