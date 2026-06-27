'''

                                            DAY 5 - PYTHON DICTIONARY DATATYPE & METHODS, SET DATATYPE & METHODS

Dictionary:
--------------------
-> it is a key value pair separated by : , and keys are unique
-> in the place of keys we jhave use immutable datatype..
-> it is a mutable type
ex:
    details = {"name":"ev",
                1:"number",
                (6,7):[1,2]}
    print(details)

Dictionary Methods:
---------------------
1.keys():
-> it is used to get all the keys from the dict.
syntax -> variable_name.keys()
ex:
    details = {"name":"ev",
           "age": 21,
           "gender":"male"}
    print(details.keys())
    
2.values():
-> it is used to get all the values from the dict.
syntax -> variable_name.values()
ex:
    details = {"name":"ev",
           "age": 21,
           "gender":"male"}
    print(details.values())
    
3.items():
-> it is used to get both key and value in a pair from the dict.
ex:
    details = {"name":"ev",
           "age": 21,
           "gender":"male"}
    print(details.items())

ex:
    details = {"name":"ev",
           "age": 21,
           "gender":"male",
           "college":"srkrec",
           "hometown":"vzm"
           }
    print(details['college'])

4.clear():
-> if we use the clear method, the dict will become clear
ex:
    details = {"name":"ev",
           "age": 21,
           "gender":"male"}
    details.clear()
    print(details)

5.update()
-> it can update the values based on keys and can add the key value they are not present.
ex:
    details = {"name":"ev",
           "age": 21,
           "gender":"male"}
    details.update({"name":"ekanthv"})
    print(details)
    details.update({"mob":"7674071873"})
    print(details)

Set:
----------------------
-> Set is a collection unordered elements that are sepearted by ,
-> set is mutable
-> can remove duplicate value by itself..
ex:
    go = {1,2,3,4,5}
    print(go)

Set Methods:
----------------------
1.union():(|)
-> it is used to combine elements from both set
Syntax -> set_1.union(set_2)
ex:
    go = {1,2,3,4}
    so = {4,5,6,7}
    print(go | so)
    print(go.union(so))

2.intersection(): (&)
->it is used to get common values from both set
ex:
    go = {1,2,3,4}
    so = {4,5,6,7}
    print(go & so)
    print(go.intersection(so))

3.Symmetric Difference(): (^)
-> it gives all differenece elements from both sets
ex:
    go = {1,2,3,4}
    so = {4,5,6,7}
    print(go ^ so)
    print(go.symmetric_difference(so))

4.add():
-> it is used to add new elements into set
ex:
    go = {1,2,3,4}
    go.add(5)
    print(go)

5.remove():
-> it is used to del elements in the set.
ex:
    go = {1,2,3,4}
    go.remove(2)
    print(go)

5.discard():
-> it is used to remove elements in the set but if the element is not present in set and if you discard it and it didn't give error.
ex:
    go = {1,2,3,4}
    go.discard(9)
    print(go)
    go.discard()
    print(go)

'''

