'''

                        DAY 27 - PYTHON CONCEPTS
                        -------------------------

Regular Expression(Regex):
---------------------------
-->regex is an sequence of char that can searching pattern
-->to use regex we have to import re module..

functions:
-----------
1.findall()
-----------
-->it will find all the char that are in the string''
eg:-
import re
txt='python is a language and also called dynamically typed'
print(re.findall('[an]',txt))

2.search()
----------
-->this search() will find the char,but it will the first sequence that found in the string...
ex:
---
import re
txt='python is a language and also called dynamically typed'
print(re.search('[a]',txt))

3.split()
---------
ex:
---
import re
txt='python is a language and also called dynamically typed'
print(re.split(' ',txt))

4.sub()
-------
ex:
---
import re
txt='python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))

5.fullmatch()
--------------
ex:
---
text = "Python123"
print(re.fullmatch(r"[A-Za-z0-9]+", text))


Metachar:
---------
1.[] - we can give range of characters and numbers for reliable functions.
-----
ex:
import re
txt='I have 100 Rupees'
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
print(re.findall('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))
print(re.search('[0-9]',txt))

2.^ - checks the first character in string it it meeting its conditions are not.
----
ex:
---
import re
txt='I am going to school'
print(re.findall('^I',txt))
print(re.search('^I',txt))

3.$ - checks the end character in string it it meeting its conditions are not.
----
ex:
---
import re
txt='I am going to school'
print(re.findall('school$',txt))
print(re.search('school$',txt))

4. .(dot) - return the strings having no. of dots the condition meets
--------
ex:
import re
txt='I am going to school'
print(re.findall('s....l',txt))
print(re.search('s....l',txt))

5.* - it return zero or more occurence by given condition.
-----
ex:
---
import re
txt='I am going to school'
print(re.findall('a.*o',txt))
print(re.search('a.*o',txt))

6.+ - it return one or more occurence by given condition.
-----
ex:
---
import re
txt='I am going to school'
print(re.findall('s.+l',txt))
print(re.search('s.+l',txt))

7.{} - 
-----
ex:
---
import re
txt='I am going to school'
print(re.findall('a.{10}',txt))
print(re.search('a.{10}',txt))

'''
import re
txt='I am going to school'
print(re.findall('a.{10}',txt))
print(re.search('a.{10}',txt))

text = "Python123"
print(re.fullmatch(r"[A-Za-z0-9]+", text))



