
# Simple interest

'''
def simple_interest (p,t, r): 
    print ('Principal is ',p)
    print ('Time is',t)
    print ("Rate of interest is ", r)

    
    si = (p*t*r)/100
    print ('the simple interest is ',si)
    return si

simple_interest(8,6,8)

'''

#Compound Interest 


def Compound_interst (p,r,t) :
    amount = p*(pow ((1+r/100),t))
    ci =  amount -p 
    print ("Compound interst is ",ci)

Compound_interst (10000,10.25,5)