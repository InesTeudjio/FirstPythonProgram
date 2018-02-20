#19. Write a Python program to get the part of a string before a specified character.
def get_Last_Part(string, char):
    x = string.find(char)
    return string[:x]
print(get_Last_Part('https:www.w3resource.com/python-exercises','-'))