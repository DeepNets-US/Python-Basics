# def add_underscores(word):
#     new_word = "_"
#     for i in range(0, len(word)):
#         # new_word = word[i] + "_" # Bug
#         # new_word += word[i] # Stil Buggy
#         new_word += word[i] + "_" # Solved
#     return new_word

# # Test the function
# phrase = "hello"
# print(add_underscores(phrase))


# Alternatives
def add_underscores(word):
    new_word = "_"
    for char in word:
        new_word += char + "_"
    return new_word

# Test the function
phrase = "hello"
print(add_underscores(phrase))

