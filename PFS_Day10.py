#prime number check 
num = 7
count = 0
for i in range(1,num+1):
    if num%i == 0:
        count += 1
if count == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


#prime number generating for given number

n = 20
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(f"{i} is a prime")

# right trainagle code
n = 5
for j in range(1,n+1):
    for i in range(1,j+1):
        print("*", end = " ")
    print()

# generate number traingle
n = 5
for j in range(1,n+1):
    for i in range(1,j+1):
        print(j, end = " ")
    print()

# generate number traingle
n = 5
for j in range(1,n+1):
    for i in range(1,j+1):
        print(i, end = " ")
    print()

# generate number sequence traingle
n = 5
count = 0
for j in range(1,n+1):
    for i in range(1,j+1):
        count += 1
        print(count, end = " ")
    print()

#armstrong number
n = int(input("enter a number: "))
all = 0
length = len(str(n))
for j in str(n):
    all += int(j)**length
if all == n:
    print(f"{all} is a armstrong number")
else:
    print(f"{all} is not a armstrong number")

# perfect number
n = int(input())
ls = []
for i in range(1,n):
    if n%i == 0:
        ls.append(i)
if sum(ls) == n:
    print("perfect number")
else:
    print("not perfect number")
    
# pyramid
num = 6
for j in range(num):
    print(" "*(num-j-1),end = " ")
    print("*" *(2*j+1))

    


