#18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.

def string_copie(string):
    return string[:3]
print(string_copie('Python'))