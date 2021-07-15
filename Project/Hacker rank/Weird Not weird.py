

month =dict()
# print( month)
month['One']='Jan'
month['two']="feb"
# print(month)
len(month)
a = month.get("One")

T = (10,20,30, 40,50)
t1=T[2:4]

'''
users = ['Rohan Das','Shubham','Skill f ','Rushikesh More']
computer = ['respbeery pi ','Android', 'iphone','100 rs wala computer']
names = ['Rushikesh' ,'prakesh' ,'soma' , 'Rau']


for i in range (0,len(users)):
    templet = 'Computer used by {} is {} gifted by {}'
    print (templet.format(users[i],computer[i],names[i]))

'''

n  = int (input('Please enter number: '))
if (n%2)== 0:
    if n in range (2,5):           
        print('Not weird'.format(n))


    elif n in range (6,20):
        print ('Weird'.format(n))

    
    elif n<20:
        print ("Not weird 0".format(n))

