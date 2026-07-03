'''

                                    DAY 9 - PYTHON LOOPS & CONTROL STATEMENTs

Loop Statements:
---------------------------
1.for loop:
-----------
-> A for loop is used to itterate over a sequence,list,tuple
ex:
    any_ = "python"
    for i in any:
        print(i)
    any_ = [1,2,3,4,5]
    for i in any:
        print(i)
    any_ = (1,2,3,4,5)
    for i in any:
        print(i)
    any = {"Name":"ev",
             "role":"students"}
    for key in any.values():
        print(key)

else in for loop:
-----------------
-> The else block will be executed after the loop, but incase the loop is breaked then it will never entered in the else block.
ex:
    any = [1,2,3,4,5]
    for val in any:
        print(val)
    else:
        print("program ended")
    
range():
---------
-> range() is a built-in function that is used to generate a sequence upto a limit
syntax -> range(start,end,step)
ex:
    for i in range(1,50):
        print(i)

2. while loop:
---------------
-> the while loop will execute until the condition is remains true.
ex:
    i =1
    while i<5:
        print(i)
        i =i+1

Control Statements:
--------------------------
1.break:
---------
-> the break is used to exit from the loop
ex:
    any = [1,2,3,4,5]
    for val in any:
        print(val)
        if val == 3:
            break
    else:
        print("program ended")
    
2.continue:
------------
-> it is used to skip the cuurent itteration from loop
ex:
    any = [1,2,3,4,5]
    for val in any:
        if val == 3:
            continue
        print(val)
    else:
        print("program ended")
    
3.pass:
--------
-> space holder
ex:
    any = [1,2,3,4,5]
    for val in any:
        pass

assert keyword:
----------------
-> it will used to check the condition , but it will raise an error incase it is false...
ex:
    num = 10
    assert num > 0
    print(f"{num} is positive number")
    assert num < 0, "has to be positive"

    age = int(input("enter your age: "))
    assert age>=18, "you must have 18 years"

'''



