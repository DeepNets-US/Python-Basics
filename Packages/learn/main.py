from learn.sublearn import name as subname
from learn.module1 import greet
from learn.module2 import depart

name = subname.name()
print(greet(name))
print(depart(name))
