#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)

def string_copies(string):
    return string[-2:]*4
print(string_copies('Python'))