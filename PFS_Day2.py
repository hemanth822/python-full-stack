'''
    operators
 --------------------
 1.Arithmetic operator
     eg: +,-,/,*,%,**
 2.Assignment operator
     eg: =,+=,-=,*=,/=,**=,%=
     -- difference between "==" and "is"
         == checks same literals or not
         is checks same object or not
     
 3.comparision operator
     eg: ==,!=,<=,>=,<,>
 4.Logical operator
     eg: and , or , not
 5.Identity operator
     eg: is , is not 
     --- "is" checks it is same object or not
 6.Membership operator
     eg: in , not in
 7.Bitwise operator
     eg: &,|,<<,>>,^,~
 
 
'''

a=4
b=5

print(a+b,a*b,a/b,a%b,a**b)
a += 3
print("a=",a)
print(a>=b and b!=a)
print(a or b)
m=[1,2]
n=m
print( m is n)
r=('hemanth')
print("h" in r)
print(4&5)
