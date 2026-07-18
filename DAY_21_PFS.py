'''

                        DAY 21 - PYTHON CONCEPTS


Self Keyword:
----------------
-> Self refers to current object....
ex:
'''
class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()
'''

constructor:
-------------
-> This Constructor initializes the object automatically when it is created...
-> 
ex:
'''
class batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
b4 = batch('Ekanth','AI&DS')
b4.display()
'''

Access Specifiers:
--------------------
protected:
-----------
ex:
'''
class fam:
    def __init__(self):
        self._name = "Ekanth"
f = fam()
print(f._name)

class batch:
    def __init__(self,name,branch):
        self._name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
b4 = batch('Ekanth','AI&DS')
b4.display()
'''
private:
-----------
ex:
'''
class Bank:
    def __init__(self):
        self.__pin = '2005'
    def display(self):
        print(self.__pin)
AC = Bank()
AC.display()
'''

Enscapsulation:
-----------------
-> Means wrapping the data and methods into a single unit(class) while
controlling access to the data
'''
class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,d_amount):
        self._balance += d_amount
        print(self._balance)
    def withdraw(self,w_amount):
        self._balance -= w_amount
        print(self._balance)
tran = atm(6000)
choice = int(input("1.Deposit\n2.Withdraw\nEnter your choice: "))

if choice == 1:
    d_amount = int(input("enter your amount to deposit: "))
    tran.deposit(d_amount)
elif choice == 2:
    w_amount = int(input("enter your amount to withdraw: "))
    tran.withdraw(w_amount)
else:
    print("invalid data!")
    
'''
'''


    


