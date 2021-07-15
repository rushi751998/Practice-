


print ('Welcome to Bank of India atm\n')

Balance = 10000
option = 3
restart = "y"
Chance = 3 
while Chance >=0 :
    pin = int (input("Enter Your PIN : "))
    if pin == (1234):
        print ('You enterd Correct pin\n ')
        while restart not in ('n','no','NO','N','No'):
            print('option 1 Check Balance :\n  ')
            print('option 2 Withdrawl :\n  ')
            print('option 3 Payin :\n  ')
            print('option 4 Return Card :\n  ')
            option = int (input('What you want ? :'))
            if option == 1:
                print ('Your Balance is : ',Balance)
                if restart in ('n','no','NO','N','No'):
                    print ('Thank you')
                    break

            elif option == 2:
                draw = float (input ('Enter amount : ' ))
                Balance = Balance- draw
                print ('Your Balance' , Balance)
                if restart in ('n','no','NO','N','No'):
                    print ('Thank you')
                    break

            elif option == 3:
                Payin = float (input ('Enter amount to Payin : ' ))
                Fund  = Balance + Payin
                print ('Your Balance' , Fund)
                if restart in ('n','no','NO','N','No'):
                    print ('Thank you')
                    break
            
            elif option == 4:
                print ('Please Wait your card will be returned')
                print ('Thank you')
                break
    elif pin!= ('1234'):
        print ("Please Enter Correct Number")
        Chance = Chance - 1
        if Chance ==0:
            print ("You have Exceed Your Limit ")
            break
                
