
# 11. Write a Python program to remove the characters which have odd index values of a given string.

def remove_odd(strrr):
    result = ''
    for i in range(len(strrr)):
        if i % 2 == 0:
            result = result + strrr[i]
    return result
print(remove_odd('fitness'))
