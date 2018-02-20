#16. Write a Python function to insert a string in the middle of a sting.

def insert_string(sting,str):
    return sting[:2] + str + sting[2:]
print(insert_string('[[]]','Python'))