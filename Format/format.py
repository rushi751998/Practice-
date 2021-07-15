
''''
a = ['rushi','akshay','saran','adi']
z = ['respbrypi' , 'android', 'iphone' ,'sastawala ' ]

for i in range (0,len(z)):
    template = "Computer used by {} is {}"
    print (template.format(a[i],z[i]))

'''



n = int(input("Please enter number : "))
if (n % 2) ==0:
    if n in range (2,5):
        print (" Not weird ".upper())
    
    elif n in range (6,20):
        print ("weird ".upper())
        
    elif n<20:
        print ("Not weird ".upper())
