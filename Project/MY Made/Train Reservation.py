'''
traveling = input ('yes or no:')
while traveling == "yes":
    passangers = int (input ('Enter the number of travellers'))
    for passangers in range (1, passangers+1):
        name = input(" Name :")
        age = input("Age :")
        sex = input ('Sex :')
        print (name)
        print (age)
        print (sex)
    
    traveling = input ("Oops!!! Forget someone : ")

'''
seat_avalible = 3
travaling = input ('Are you Travalling Yes or No : ' )
while travaling == "yes":
    passangers = int (input("Enter the number of passanger : " ))
    check = (seat_avalible - passangers)
    seat_avalible = (seat_avalible-passangers)
    if check <=1:
        print ('Sorry there is no seat available .... Please try again sometime')
        break
    elif check>=1:
        print (" Congratluation There is seat available")
    
    for passangers in range(1,passangers +1):
        name = input ('Name : ')
        Age = input ('Age : ')
        if Age in range [0:10]:
            print ('There is no ticket for kids')

        elif Age in range [10:20]:
            print ('Ticket for the kids is 20rs')

        Sex = input ("Male or Female : ")
        
        #print('Seat remaning : ',seat_avalible)
    
    Conform = input ('conform ticket (yes or no) : ')        
    if Conform == ('yes' ) :
        print(name)
        print(Age)
        print(Sex)
        print ('Seat Remamaing : ', seat_avalible)
        print ('Thank you')
    elif Conform != ('yes'):
        input('Please report problem ')
        print ("Our team member will call you\n Thank for visiting")
    break
    

'''           
elif travaling!= "yes"
    print ("Seat available : ",seat_avalible)
    break
'''