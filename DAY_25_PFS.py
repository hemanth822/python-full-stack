'''

                    DAY 25 - PYHTON CONCEPTS

Error Handling
-----------------
syntax error:
--------------
for j in range(1,10):
    print(j)

o/p -- SyntaxError

indentation error:
-------------------
    a = 20
for j in range(a):
    print(j)
else:
print()

o/p -- IdentationError

Value Error:
-------------
num = int(input("enter a num: "))

o/p -- ValueError (if we enter different datatype)

Expection Handling
-------------------
try:
-----
The try block will test the code for error

syntax -- try:

except:
--------
This except let us handle the errors in the code
syntax -- except:

ex:
try:
    print(num)
except NameError:
    print('will get name error')

ex:
try:
    num = int(input())
    num2 = int(input())
    print(num/num2)
except ZeroDivisionError:
    print('will get a zerodivision error')
except ValueError:
    print('will get a Value error')

else:
------
if the try block does not have any error than the else block will execute.
ex:
try:
    num = int(input())
    num2 = int(input())
    print(num/num2)
except ZeroDivisionError:
    print('will get a zerodivision error')
except ValueError:
    print('will get a Value error')
else:
    print('no error')

finally:
-----------
The finally block will execute either code contain errors or not.
ex:
try:
    num = int(input())
    num2 = int(input())
    print(num/num2)
except ZeroDivisionError:
    print('will get a zerodivision error')
except ValueError:
    print('will get a Value error')
else:
    print('no error')
finally:
    print('End')

'''
    

