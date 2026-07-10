# ATM code

details = { "Name" : "HEMANTH",
            "ATM PIN" : "1234",
            "Balance" : 20000 }
print("-----------WELCOME------------")
print()
attempt = 3
Transaction=[]
count=1
while attempt>0:
    user_pin = input("pls enter your 4 digit pin: ")
    if len(user_pin) == 4:
        if user_pin in details['ATM PIN']:
            while count ==1:
                choice = int(input("1.withdraw \n2.deposit \n3.balance \n4.Change pin \n5.Transaction history\nEnter your choice: "))
                if choice == 1:
                    withdraw_m = int(input("pls enter amount to withdraw: "))
                    if withdraw_m <= details['Balance'] and withdraw_m%100 == 0:
                        details['Balance'] -= withdraw_m
                        
                        Transaction.append('withdraw amount :'+ str(withdraw_m))
                        print(f"Withdrawal succesfully {withdraw_m} and balance is {details['Balance']}")
                    
                    else:
                        print("entered amount is insufficient or change is not withdrawed")
                elif choice == 2:
                    deposit_m = int(input("pls enter amount to deposit: "))
                    if deposit_m%100 == 0:
                        details['Balance'] += deposit_m
                        Transaction.append('deposit amount :'+str(deposit_m))
                        print(f"succesfully deposited {deposit_m} and balance is {details['Balance']}")
                    else:
                        print("change is not Deposited")
                elif choice == 3:
                    print(f"Your balance is {details['Balance']}")
                elif choice == 4:
                    old_pass=input('Enter old PIN: ')
                    
                    if  old_pass == details['ATM PIN'] :
                        
                        new_pass=input('Enter new PIN: ')
                        if len(new_pass)==4:
                            confirm_pass=input('Confirm new PIN: ')
                            if new_pass==confirm_pass:
                                details['ATM PIN']=new_pass
                            else:
                                print('PIN mismatch')





                        
                        else:
                            print('Invalid Enter four digits') 
                    else :
                        print('Wrong pin')
                elif choice == 5 :
                    if len(Transaction)==0:
                        print('No recent transactions')
                        print('Balance : ',details['Balance'])
                    else:
                        for i in Transaction:
                            print(i)
                        print('Balance : ',details['Balance'])
                else:
                    print('Invalid choice!')
                count=int(input('1.Continue\n2.Exit: '))
            else:
                print('Thank you for using!')
                break

            
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Incorrect pin and you have {attempt} left.")
            else:
                print("Your card is blocked and contact the bank.")
                break
    else:
        print("pls enter only 4 digit pin")
