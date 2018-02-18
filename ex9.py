# 9. Write a Python program to remove the nth index character from a nonempty string.

def remove_char(strr,n):
    first_part = strr[:n]
    second_part = strr[n+1:]
    strr = first_part + second_part
    return strr
print(remove_char('Python',0))
print(remove_char('Python',4))