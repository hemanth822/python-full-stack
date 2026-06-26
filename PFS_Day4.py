'''

                                            DAY 4 - PYTHON LIST DATATYPE & METHODS, TUPLE DATATYPE & METHODS

List:
----------------
-> List is a collection of different datatypes that are enclosed in [] separated by commas(,).
-> List is muttable
ex:
    all_type = [1,'python',[1,2]]
    print(all_type)

    imuttable:                                mutable:
    -> datatype cannot be modified            -> datatype can be modified
    ex:                                       ex:
        so = 'python is best'                    any_ = [1,2,3,4]
        print(so.replace('pyhton','java'))       print(any_)
        print(so)                                any_.append(5)
                                                 print(any_)

list methods:
----------------
1.append():
-> This is used to add new item into list, but it will add in the last index position
ex:
    any_ = [1,2,3,4]
    print(any_)
    any_.append(5)
    print(any_)
    any_.append('python')
    print(any_)

2.extend():
-> This is also add a item in the last index position, but it will give each value in the each index position
-> this will take only iterable...
ex:
    any_ = [1,2,3,4]
    print(any_)
    any_.extend([23,90])
    print(any_)
    any_.extend('python')
    print(any_)

    any_ = [1,2,'python is a language',[45,78,'java is a language',[1,23],90],'hello']
    print(any_[3][3][1])

3.pop():
-> it used to del the value from the list, but it will del based on the index position.
syntax -> variable_name.pop(index_position)
ex:
    any_ = [1,2,45,78,23,90]
    any_.pop(5)
    print(any_)

4.remove():
-> it is used to del the value from the list, but it del direct value from list.
syntax -> variable_name.remove(value)
ex:
    any_ = [1,2,45,78,23,90]
    any_.remove(90)
    print(any_)
    
Tuple:
----------------
-> tuple is a collection of different dattypes represent in () and seperated by , (commas).
-> it is a immutable.
ex:
    any_ = (1,2,'python',[6,7],(67,90))
    print(any_)

Tuple methods:
----------------
1.index():
-> Returns the index (position) of the first occurrence of the specified element.
ex:
    t = (10, 20, 30, 20)
    print(t.index(20))
    
2,count():
-> Returns the number of times the specified element appears in the tuple.
ex:
    t = (10, 20, 30, 20)
    print(t.count(20))

'''




