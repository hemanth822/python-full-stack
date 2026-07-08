'''

                DAY 13 - PYTHON PROGRAMMING COCEPTS

Passing by value:
---------------------
ex:
    def some(a):
        for j in a:
            print(j)
    some([1,2,3])
    def some(a):
        for j in a:
            print(j)
    some((1,2,3))

Passing by reference:
---------------------
ex:
    a = [1,2,3]
    def some(a):
        for j in a:
            print(j)
    some(a)

return keyword:
-------------------
-> In a function, if a return is executed then it will exit from the function with certain return values.
ex:
    def mufunc(b):
        return 5+myfunc(b)
    a = myfunc(10)
    c = myfunc(100)
    print(a)
    print(c)

To Print all Built-in Function:
-----------------------------------
import builtins

builtin_functions =[
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"Total built-in functions are {len(builtin_functions)}")

Recursive Function:
---------------------
-> Recursive function that calls itself repeatedly until a specified condition is met....
syntax: ->  def func_name(parameter):
                if condition: -> base case
                    return statement
                else:
                    return statement
            print(func_name(arguments))
            
ex:
    def func_name(num):
        if num == 1:
            return 1
        else:
            return num* func_name(num-1)
    num = 5
    print(func_name(num))

'''

