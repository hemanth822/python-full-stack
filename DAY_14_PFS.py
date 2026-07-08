'''


                      DAY 14 - PYTHON CONCEPTS

Lambda Function:
-------------------
-> This is also called as annonymous function
-> a lamda function can take n number of arguments but having onlly one expression
syntax -> lambda arguments : expression
ex:
    some = lambda an,so,why : an * so - why
    print(some(10,1,7))

filter():
-----------
-> the filter is a built-in function used to filter elements from an itterables such as list, tuple and set based on condition.
syntax -> filter(function, itterable)

-> This filter() function returns filter object so we can convert that into other types like list,set and tuple.
ex:
    nums = [1,2,3,4,5]
    rev = filter(lambda a: a%2 == 0,nums)
    print(list(rev))

    nums = [1,2,3,4,5]
    rev = filter(lambda a: a%2 != 0,nums)
    print(list(rev))

List comprehension:
--------------------
-> This offers a shoter syntax when we want to create a new list from the old list
syntax -> variable_name = [expression loop condition]
ex:
    old = [1,2,3,4,5,6]
    new = [j for j in old if j%2 == 0] # j is expression, for and if are loop , conditions 
    print(new)

dictionary comprehension:
--------------------
-> This offers a shoter syntax when we want to create a new dictionary from the old dictionary
syntax -> variable_name = {expression loop }
ex:
    old_dict = {}
    new_dict = {i:j for (i,j) in old_dict.items() if j%2 == 0}
    print(new_dict)

'''
