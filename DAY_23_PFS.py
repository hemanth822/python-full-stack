
Polymorphism:
--------------------------
-->it means many forms
--> it allows same method, function or operator to perform different
tasks depending on the same object...

Types:
1.Method Overloading.
----------------------
-->It means having multiple methods with the same name but different parameters.

class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
obj = cal()
obj.add(4,7,)

class cal:
    def add(self,num,num_2=0):
        print(num + num_2)
        def add(self,num,num_2=0):
           print(num + num_2+num_3)
obj = cal()
obj.add(45,67)
obj.add(4,7)


2.Method overriding-
--------------------
->method overriding occurs wnen child class provides its own implemenetation of a already defined in its parent class
class animal:
    def sound(self):
        print("Animal make sound")
class dog(animal):
    def sound(self):
       print("Dogs barks")
d = dog()
d.sound()


3.operator overload
->this allows operators(+,-,*) to work differerntly for user_defined objects

class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = student(56)
s2 = student(67)
print(s1 + s2)

class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = student(56)
s2 = student(67)
print(s1 + s2)

data Abstration
----------------
->data Abstration is the process of hiding implementation deatails details and showing only the essential to the user
Eg--
->ATM
->CAR
->APP
from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def display(self):
        raise NotImplementedError('subcalss must imlemnet interest()')
class SBI(bank):
    def interest(self):
            print('SBI interest Rate: 6.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 5.5%')
class ICICI(bank):
    def interest(self):
        print('ICIC interest Rate: 6.9%')
banks = [SBI(),HDFC(),ICICI()]
for j in banks:
    j.interest()




from abc import ABC, abstractmethod
class bank:
    @abstractmethod
    def display(self):
        raise NotImplementedError('subcalss must imlemnet interest()')
class SBI(bank):
    def interest(self):
            print('SBI interest Rate: 6.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 5.5%')
class ICICI(bank):
    def interest(self):
        print('ICIC interest Rate: 6.9%')
banks = [SBI(),HDFC(),ICICI()]
for j in banks:
    j.interest()




















    
