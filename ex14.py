
# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form

items = input("Input comma separated sequence of words")
words = items.split()  #breakdown the string into a list of words
words.sort()
for word in words:
    print(word)