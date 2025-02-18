import matplotlib.pyplot as plt

fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4,
}

plt.bar(fruits.keys(), fruits.values())
plt.title('Fruits & Strengths')
plt.xlabel('Fruits')
plt.ylabel('Strength')
plt.show()
