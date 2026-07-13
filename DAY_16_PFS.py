'''

                        DAY 16 - PYTHON GENERATOR CONCEPTS

Generators:
----------------
-> This generator is special function that returns the iterator, instead of returning all the values at once....
-> Here we are going to use yield keyword
ex:
'''
def some():
    yield 1
    yield 2
    yield 3
so =some()
print(next(so))
print(next(so))
print(next(so))

'''
working of generator:
------------------------
-> when a function is called
-> it does not execute the function immediately.....
-> it will returns the generator object
-> Then the function will pauses at each yield.....
-> when the next() is called again, execution resumes from where it stopped
ex:
'''
def demo():
    print("Start")
    yield 1

    print("Middle")
    yield 2

    print('End')
    yield 3
how = demo()
print(next(how))
print(next(how))

def how(so):
    for i in range(so):
        yield i*i
any = how(5)
print(next(any))
print(next(any))
print(next(any))
print(next(any))
print(next(any))

'''
Without Generator:
------------------
ex:
'''
def sqt(n):
    for j in range(n):
        print(j*j)
sqt(5)

'''
Function & Generator difference:
--------------------------------------
function:
-----------
-> Return
-> Return complete result
-> Function will end after the return the values
-> More memory usage
-> This function never resume 

Generator:
-----------
-> yield
-> Return one value at once
-> Pauses after every yield
-> Less memory usage
-> Resumes after next()

yield keyword:
--------------
-> This will Produce the value
-> but the yield pauses the function
-> yield will save the functions current state
-> yield will continue where it stopped.....

next() keyword:
----------------
-> the next() function is used to retrive the next value from an generator
ex:
'''
def how(so):
    for i in range(so):
        yield i*i
any = how(5)
print(next(any))
print(next(any))

'''
StopIteration:
---------------
-> Calling next() function after all values retrive then it willl raise StopIteration exception
ex:
'''
def how(so):
    for i in range(so):
        yield i*i
any = how(5)
print(next(any))
print(next(any))

'''
ex:
'''
def loop(n):
    for i in range(n):
        yield i
how = loop(5)
print("ex:")
print(next(how))
print(next(how))
'''
Generator expression:
-----------------------
-> The generator expression is similar to a list comprehension but uses parenthesis () instead of []
ex:
'''
gen = (x*x for x in range(5))
print(next(gen))
