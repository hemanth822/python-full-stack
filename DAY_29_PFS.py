'''

                    DAY 29 - PYTHON CONCEPTS
                    ------------------------

Matplotlib
------------
Matplotlib library is an python library that provides functionality to
charts, graphs, bar and data visualization
ex:
---
line pot
---------
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,5]

plt.plot(x,y)
plt.show()

bar plot
---------
import matplotlib.pyplot as plt
x = [2026,2025,2024,2023,2022]
y = [120,150,135,97,70]

plt.bar(x,y,color = 'blue',edgecolor='black')
plt.title('Car Sales')
plt.xlabel('Year')
plt.ylabel('Number of cars')
plt.show()

pie chart
----------
import matplotlib.pyplot as plt
subjects = ['python','java','C']
stu = [69,13,50]
plt.pie(stu,labels=subjects,colors=['red','white','purple'],autopct='%1.1f%%')
plt.legend(subjects)
plt.title('Courses')
plt.show()

scatter plot
-------------
import matplotlib.pyplot as plt
x = ['python','java','C']
y = [69,13,50]
plt.scatter(x,y,color='red')

plt.title('Car Sales')
plt.xlabel('Year')
plt.ylabel('Number of cars')
plt.show()

ex:
----
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C"]
marks = [85, 78, 92]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(subjects, marks, marker='o')
plt.title("Line Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.subplot(2, 2, 2)
plt.bar(subjects, marks)
plt.title("Bar Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.subplot(2, 2, 3)
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.title("Pie Chart")

plt.subplot(2, 2, 4)
plt.scatter(subjects, marks)
plt.title("Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()

histogram
----------
ex:
---
import matplotlib.pyplot as plt
y =[10,20,30,40]

plt.hist(y,bins=20)
plt.title('Car Sales')
plt.xlabel('Year')
plt.ylabel('Number of cars')
plt.show()
'''

