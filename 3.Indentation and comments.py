# 1.Indentation

a = 5
if (a==5):
    print("True")   #Right Indentation

# if (a==5):
# print("True") #wrong indentation

# 2.Comments

print ("Hello") #This is a program - Inline comments


print("Vanakkam")
#Above code is the most simple program in python - Single line comments

"""
Hi this a multi line comments. 
Usually exists in program that are ignored by compilers and interpretors.
"""

#Doc strings

def f1():
    """
    this a part of docstring 
    multiline
    format
    """
    name="Karuna"
    print("Hello",name)

    """
    This is not a part of 
    docstring
    """
    print(1+5)

f1()

print(f1.__doc__)