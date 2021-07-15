grocery = ['bread','milk','butter']
for item in enumerate(grocery):
    print(item)

print('\n')       #n is used for taking new line or brake
for count, item in enumerate(grocery):
    print(count,item)

print('\n')     #n is used for taking new line   or brake
# Changing default start value



for count , item in enumerate(grocery,100):
    print(count,item)
