'''

                                DAY 22 - PYTHON CONCEPTS

Inheritance:
-------------
-> Inheritance is an oop concept where one class (child/derived) acquired the
properties and methods of another class(parent/base)
ex:
'''
class parent:
    pass
class child(parent):
    pass
'''
1.single inheritance:
------------------------
a child class inherits from one parent is single inheritance
ex:
'''
class animal:
    def sound(self):
        print('animals make sound')
class dog(animal):
    def barks(self):
        print("dog barks")
d = dog()
d.sound()
d.barks()

class father:
    def land(self):
        print('5 acres o fland')
class son(father):
    def flat(self):
        print('3bhk flat')
s = son()
s.land()
s.flat()
'''
Multiple Inheritance
----------------------
A child inherits more than one parent is called multiple inheritance
ex:
'''
class father:
    def skills(self):
        print('Driving')
class mother:
    def talent(self):
        print("cooking")
class brother:
    def learn(self):
        print("games")
class son(father,mother,brother):
    def mine(self):
        print("coding")
s = son()
s.skills()
s.talent()
s.learn()
s.mine()
'''
multi-level inheritance:
-------------------------
one child class becomes the parent for another class.
ex:
'''
class gfather:
    def house(self):
        print("own house")
class father(gfather):
    def flat(self):
        print("new 3bks house")
class son(father):
    def car(self):
        print('have a car')
s = son()
s.house()
s.flat()
s.car()
'''
Hierarchal inheritance:
-------------------------
-> Multiple child inherita=s from the same parent
ex:
'''
class mother:
    def gold(self):
        print('10kg gold')
class varshika(mother):
    def show(self):
        print('will get 5kgs ')
class vyshu(mother):
    def show_2(self):
        print('will get remaining 5kgs')
vr = varshika()
vy = vyshu()
vr.gold()
vr.show()
vy.gold()
vy.show_2()
'''
Hybrid inheritance:
--------------------
-> This is the combination of two or more types of inheritance
ex: multiple + multi-level
'''
class A:
    def methodA(Self):
        print('Class A')
class B(A):
    def methodB(Self):
        print('Class B')
class C(A):
    def methodC(Self):
        print('Class C')
class D(B,C):
    def methodD(Self):
        print('Class D')
so = D()
so.methodA()
so.methodB()
so.methodC()
so.methodD()
'''
super():
-----------
-> This super() function is used to access the parent vlass mtehods or
constructor in the child class
ex:
'''
class parent:
    def show(self):
        print('Parent method')
class child(parent):
    def show(self):
        super().show()
        print('child class')
chi = child()
chi.show()
'''
'''
class person:
    def __init__(self,name):
        self.name = name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        print(self.name)
        print(self.roll)
an = student('Ekanth',95)
an.display()
    
        
