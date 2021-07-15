
'''
count=0


while count <5:
    print (count)
    count = count+2


#print ("Good BYE")
'''


'''
import random
n =20
guesss_number =  int(n * random.random())+1
guess = 0
while guess != guesss_number:
    guess = int(input("Enter Number : "))
    if guess >0 :
        if guess > guesss_number:
            print ("It is smaller number")
        elif guess<guesss_number:
            print ("It is larger number")
            
    else:
        print ("U Give up !!!")
        break
else :
    print(" Congralutation u made it ")
    '''

'''
count = 0
while True:
    print (count)
    count +=1
    if count >= 5:
        break
'''

print(" Welcome to Bank of india's ATM")
restart = ('Y')
Chance  = 3
Balance  = 67.14
while Chance >=0:
    pin = int (input("Please enter your pin :"))
    if pin == (1234):
        print(" You enterd pin Correctly\n")
        while restart  not in ('n',"NO",'no',"N"):
            print ('Please Press 1 for your Balance\n')
            print ('Please Press 2 for Make withdraw\n')
            print('Please Press 3 to Pay in \n')
            print ('Pleass Press 4 To Return Card\n')
            option = int (input("What would you like to choose : "))
            if option ==1:
                print('Your balance is : ',Balance,'\n')
                restart = input('Would You like to back?')
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break
            elif option==2:
                option2 = ("y")
                withdrawl = float(input('How muchwould you like to withdraw ? \n'))
                if withdrawl in [10,20,40,60,100]:
                    Balance = Balance- withdrawl 
                    print('Your Balance is now : ',Balance)
                    restart = input('Would You like to go back?')
                    if restart in ('n','NO','no','N'):
                        print('Thank You')
                        break
                elif withdrawl == 1:
                    withdrawl = float(input('Please Enter Desired amount : '))
            
            elif option==3:
                Pay_in = float(input('How much would you like to pay in ?'))
                Balance = Balance + Pay_in
                print('Your Balance is', Balance)
                if restart in ('n','NO','no','N'):
                    print('Thank You')
                    break

            elif option == 4:
                print ('Please Wait Your Card is Returened...\n')
                print('Thank you For Servicr')
                break

            else:
                print('Please enter Correct Number.\n')
                restart = ('y')
                 
    elif pin != ('1234'):
        print ('Incorret Password')
        Chance  = Chance-1
        if Chance == 0:
            print ('\n No more tries')
            break   
