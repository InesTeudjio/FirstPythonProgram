# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

string1, string2 = 'abc' , 'xyz'
new_string1 = string2[:2] + string1[2:]
new_string2 = string1[:2] + string2[2:]
string3 = new_string1 + ' ' + new_string2
print(string3)