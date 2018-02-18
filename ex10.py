# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def change_char(stringg):
    stringg = stringg[-1: ] +stringg [1:-1] + stringg[ :1]
    return stringg
print(change_char('JESUS'))