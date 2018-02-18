# 6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def add_string(str1):
    length = len(str1)

    if length > 3:
        if str1[-3:] == 'ing':
            str1 += 'ly'
        else:
            str1 += 'ing'

    if length < 3:
        str1 = str1

    return str1

print(add_string('smilling'))
print(add_string('love'))
print(add_string('not'))