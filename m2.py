import Methods
import pyqrcode
import png
'''
print(dir(Methods))

print(type(Methods.employees))
print(Methods.details.keys())
Methods.employees("hoo",'haa',department='cse')
Methods.details.update({'batches':[1,2,3],'employee':200})
print(Methods.details)
'''
#biult in modules-->math,random,os,time,datetime
#we downlod modules-->pypi(python package index)
#biuld a qrcode  scanner using python -->linkedin url
#pyqrcode,pypng(pypi.org)

link="https://www.linkedin.com/in/kittali-hemanth-kumar/"
qr=pyqrcode.create(link)
print(qr)
qr.png('mqr.png',scale=10)

