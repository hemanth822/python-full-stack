# remove duplicates

nums = [23,4,6,23,7,4]
empty = []
def remove_dup(nums,empty):
    for j in nums:
        if j not in empty:
            empty.append(j)
    print(empty)

remove_dup(nums,empty)


#prime numbers

nums = int(input("enter your number: "))
count = 0
def prime(nums,count):
    for i in range(1,nums+1):
        if nums%i == 0:
            count += 1
    if count == 2:
        print(f"{nums} is a prime number")
    else:
        print(f"{nums} is not a prime number")

prime(nums,count)

#count the number of words
string = input("enter your sentence: ")
count = 0
def count_words(string,count):
    a = string.split()
    for i in a:
        count += 1
    print(count)
count_words(string,count)

#count upper an lower characters

string = input("enter your sentence: ")
cap_count = 0
small_count = 0
space_count = 0
def cap_small(string,cap_count,small_count,space_count):
    for i in string:
        if i.isupper():
            cap_count += 1
        elif i.islower():
            small_count += 1
        else:
            space_count += 1
    print(f" there are total {cap_count} number caps")
    print(f" there are total {small_count} number caps")
    print(f" there are total {space_count} number caps")
cap_small(string,cap_count,small_count,space_count)
