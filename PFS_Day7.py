'''

                            DAY 7 - PYTHON INPUT FORMATTING

Input formatting from user:
---------------------------------
input():
-> the input() function is used to take input from user...

1.int:
-> to take integer values.
ex:
    num = int(input("enter a number: "))
    a = int(input("enter a number: "))
    print(num+a)

2.string:
-> to take string values.
ex:
    a = input("enter character: ")
    print( a ,' ','varma')

3.float:
-> to take decimal values.
ex:
    fl = float(input("enter salary:")
    print("fl" ,'is your salary')

4.list:
-> to take values into list using map 
ex:
    group = list(map(int,input().split()))
    print(group)
    group_ = list(input().split())
    print(group_)

5.tuple:
-> to take values into tuple using map
ex:
    group = tuple(map(int,input().split())
    print(group)
    group_ = tuple(input().split())
    print(group_)

*eval():
ex:
    num = eval(input("enter: "))
    print(type(num))

*fstring/doc string:
ex:
    name = input("enter your name: ")
    age = int(input("enter your age: "))
    print(name , " your age is " , age)
    print(f"{name} your age is {age}")
    print(f"{name} your age is {age+3}")

*modulus format(%):
ex:
    print("my name is %s and i'm %d years old", %(name,age))


'''
