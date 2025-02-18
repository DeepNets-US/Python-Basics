from helpers.string import shout
from helpers.math import area

l,b = 5, 10
res = area(l, b)
prompt = f"the area of {l}-by-{b} is {res}."
print(shout(prompt))
