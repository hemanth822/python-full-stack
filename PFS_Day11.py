
# palindrome

a = input("Enter word: ")
b = ""
for j in a:
    b = j+b
if b==a:
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")

# Fibanacci series

a = 0
b = 1
limit = int(input("enter a number: "))
print(a, b, end =" ")
for i in range(1,limit+1):
    all = a+b
    a = b
    b = all
    print(all, end=" ")

# Calculator code
a = int(input("enter first number: "))
b = int(input("enter second number: "))
user = int(input("\n1.add \n2.sub \n3.mul \n4.div \n5.pow \nEnter your choice: "))
if user == 1:
    print(a+b)
elif user == 2:
    print(a-b)
elif user == 3:
    print(a*b)
elif user == 4:
    print(a/b)
elif user == 5:
    print(a**b)
else:
    print("Enter correct choice!!!")

# Table generator
table = int(input("enter number to get number table: "))
limit = int(input("enter upto how many numbers to print: "))
for i in range(1,limit+1):
    print(f"{table} x {i} = {table*i}")

# perfect number

a = int(input("enter a number: "))
total = 0
for i in range(1,a):
    if a%i == 0:
        total += i
if total == a:
    print(f"{a} is a perfect number")
else:
    print(f"{a} is not a perfect number")

# ATM code

details = { "Name" : "Ekanth",
            "ATM PIN" : "2005",
            "Balance" : 100000 }
print("-----------WELCOME------------")
print()
user_pin = input("pls enter your 4 digit pin: ")
if len(user_pin) == 4:
    if user_pin in details['ATM PIN']:
        choice = int(input("1.withdraw \n2.deposit \n3.balance \nEnter your choice: "))
        if choice == 1:
            withdraw_m = int(input("pls enter amount to withdraw: "))
            if withdraw_m <= details['Balance'] and withdraw_m%100 == 0:
                details['Balance'] -= withdraw_m
                print(f"succesfully withdraw {withdraw_m} and balance is {details['Balance']}")
            else:
                print("entered amount is insufficient or change is not withdrawed")
        elif choice == 2:
            deposit_m = int(input("pls enter amount to deposit: "))
            if deposit_m%100 == 0:
                details['Balance'] += deposit_m
                print(f"succesfully deposit {deposit_m} and balance is {details['Balance']}")
            else:
                print("change is not withdrawed")
        else:
            print(f"Your balance is {details['Balance']}")
            
    else:
        print("pls enter correct 4 digit pin")
else:
    print("pls enter only 4 digit pin")


        
    
