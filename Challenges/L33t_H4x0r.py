mapping = {
    "a":"4",
    "b":"8",
    "e":"3",
    "l":"1",
    "o":"0",
    "s":"5",
    "t":"7"
    }

text = input("Enter some text: ")
new_text = text
for key, num in mapping.items():
    new_text = new_text.replace(key, num)
print(new_text)
