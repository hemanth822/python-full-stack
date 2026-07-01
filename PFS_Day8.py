'''

                            DAY 8 - PYTHON CONDITION STATEMENTS

1.Condition Statements:
------------------------------
if -> it is used to check condition is true or not
ex:
    num =n10
    if num%2==0:
        print(f"{num} is a even number")
        
if-else -> else is the fall-back statement incase the if condition is false, then this else will be executed
ex:
    num = int(input('enter no: '))
    if num%2==0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")

    ekanth_SBI_details = ("ATM PIN":1981)
    pin = int(input("enter your 4 digit ATM pin: )
    if pin == ekanth_SBI_details['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("You Have entered incorrect pin")

        

nested if -> nested if contains if block in if statement 
ex:
    ekanth_SBI_details = {"ATM PIN":'1981'}
    pin = input("enter your 4 digit ATM pin: ")
    if len(pin)==4:
        if pin in ekanth_SBI_details["ATM PIN"]:
            print("Welcome to SBI ATM")
        else:
            print("You have entered incorrect pin")
    else:
        print("please enter only 4 digit pin")

    
elif -> elif is used for more options for the same condition.
ex:
    num = int(input("Enter Your Marks:"))
    if num >= 90:
        print("A+")
    elif num >= 80:
        print("A")
    elif num >=70:
        print("B")
    elif num >= 60:
        print("C")
    elif num >= 50:
        print("D")
    elif num >= 40:
        print("E")
    else:
        print("F")

'''
    


