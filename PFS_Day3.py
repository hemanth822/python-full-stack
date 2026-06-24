'''
    Data types
------------------
1. int    - eg: 1,2,3
2. float  - eg: 1.2,3.333
3. str - eg: "man", "go"
    ->string is immutable

    Concatenation     
----------------------
-> Concatenation will combine the string by using "+" operator

    Indexing
----------------
-> This is used to acces the particular char in string or a value in the list by passing the index position value
-> Index start from 0.
-> we have reverse indexing to count the position from last char to first.
    eg: a[-2], a[2]

    list Methods
--------------------
1. append()
2. extend()
3. pop()
4. remove()

    String methods
---------------------
1. replace() - Used to replace a substring in that particular string.
                eg: print(a.replace("old_string", "new_string",count))
                
2. join()    - Used to add new substring after each substring in the string
                eg : print("@".join(a))
                
3. split()   - Used to divide the string into different parts by the string that we pass
                eg: print(a.split(" "))  -> it will split at every space ( " " )

4. count()   - Used to count the repitition of a char in the string
                eg: a.count("s")


    Built-in Functions
---------------------------
1. len() - this will give the length of the string or list
2. max() - this will get the max char in the string according to ASCII values
3. min() - this will give min char in the string according to ASCII values

'''




a="hello world"
#print(len(a))
#print(a[-1:-5])
print(a.replace('l','m',2))
print("@".join(a))
b= a.split()
print(a.count(" "))
print(b)
print(len(b))
print(len(a),max(a),min(a))

time ="16:56"
print(time)
parts= time.split(":")
print(parts)
print(str(int(parts[0])-12)+":"+parts[1])




