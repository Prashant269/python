Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # print hello word
>>> print("hello world")
hello world
>>> 
=============================== RESTART: Shell ===============================
>>> num=("enter the number")
>>> num=input("enter the number")
enter the number12
>>> num1=input("enter the number")
enter the number12
>>> num3=int(num)+ int(num2)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    num3=int(num)+ int(num2)
NameError: name 'num2' is not defined
>>> num3=int(num)+ int(num1)
>>> print(num3)
24
>>> 
