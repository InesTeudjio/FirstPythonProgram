#21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert_string(str):
    Upper = str.upper()
    if str[:4] == Upper:
        str = str.upper()
    return str.upper()

print(convert_string('PYTHon'))
