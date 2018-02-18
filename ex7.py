#7. Write a Python program to find the first appearance

def not_poor(str2):
    snot = str2.find('not')
    sbad = str2.find('poor')

    if sbad > snot:
        str2 = str2.replace(str2[snot:(sbad+4)],'good')

    return str2
print(not_poor('The lyrics is not that poor!'))
