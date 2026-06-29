'''

                                DAY 6 - PYTHON TYPE CONVERSIONS

Type Conversionns:
------------------------
-> This is process of conerting one data type to another data type....

built-in functions:
------------------------
-> str()
-> float()
-> int()
-> list()
-> dict()

Int --> String, float
-> we can converts integer to float and float values
ex:
    num = 89
    print(type(num))
    so = str(num)
    print(type(so))

    fl = float(num)
    print(type(fl))


Float --> String, Integer
-> we can convert float to string and integer values
ex:
    fl = 8.9
    print(type(fl))
    so = int(fl)
    print(type(so))

    string = str(fl)
    print(type(string))

String --> Integer, Float, List, tuple
-> we cam convert string to Integer, Float, List and tuple.
ex:
    hi = '78'
    nu = int(hi)
    print(nu) # string to int

    h2 = '7.7'
    fl = float(h2)
    print(fl) # string to float

    any_ = "python"
    conv = list(any_)
    print(conv) # string to list
    
    conv2 = tuple(any_)
    print(con2) # string to tuple

List --> String,Tuple, Dictionary
-> we can conert List to string,list and dictionary
ex:
    var = ['p','y','t','h','o','n']
    text = "".join(var)
    print(text)

    tup = tuple(var)
    print(tup)

    pyth = [('a',1),('b',2)] 
    conv = dict(pyth)
    print(conv)

Tuple --> String, List
-> we can convert tuple to string and list
ex:
    fam = ('h','i')
    so = "".join(fam)
    pirnt(so)

    so1 = list(fam)
    print(so1)

'''
