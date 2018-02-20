# 20. Write a Python function to reverses a string if it's length is a multiple of 4.
def reverse_str(string):
    if len(string) % 4 == 0:
        new_string = string[::-1]
    return new_string
print(reverse_str('I lov Python'))