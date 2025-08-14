# print("Conditions")

# print("Difference between AND and OR")

# '''
# AND - Bad Guy  -First False and Last True
# OR  - Good Guy -First True and Last False
# '''
# print("---------------------------------")

# a = int(input("Enter the number a:"))
# b= int(input("Enter the number b:"))

# if (a<b):
#     print("a is lesser than b")
# elif(a>b):
#     print("a is greater than b")
# else:
#     print("a is equal to b")

# print("=================================================================")

# var = input("Enter the letter:")
# if var in ["a","e","i","o","u"]:
#     print("vowels")
# else:
#     print("constants")

# print("=================================================================")

# '''
# * None
# * False
# * 0 
# * Empty sequence-list,tuple,"",''
# * Empty mappings-{}
# * User defined types where the __bool__ or __len__ methods return 0 or False

# ALL OTHER VALUES IN PYTHON EVALUATE TO TRUE.

# '''

# print("=================================================================")

# print("Truthy values")

# if True:
#     print("Yes")

# if False:
#     print("It does not print and execution does not come to this line")

# if None:
#     print("It does not print and execution does not come to this line")

# if 1:
#     print("Yes")

# if 0:
#     print("It does not print and execution does not come to this line")

# if not 1:
#     print("It does not print and execution does not come to this line")

# if [3,4,5]:
#     print("Yes [3,4,5]")

# if []:
#     print("It does not print and execution does not come to this line")

# if (7,8):
#     print("Yes (7,8)")

# if ():
#     print("It does not print and execution does not come to this line")

# if {1,2}:
#     print("Yes {1,2}")

# if {}:
#     print("It does not print and execution does not come to this line")

# if 'abc':
#     print("Yes 'abc'")

# if '':
#     print("It does not print and execution does not come to this line")

# if "":
#     print("It does not print and execution does not come to this line")

# if ' ':
#     print("Yes but able to print.So repr in next line")
#     print(repr(" "))

# if ("Data science"):
#     print("Yes DS ")

# if (5-5):
#     print("It does not print and execution does not come to this line")

# if (0.0):
#     print("It does not print and execution does not come to this line")

# if 1j:
#     print("Yes 1j is an content")

# if 0j:
#     print("It does not print and execution does not come to this line")

# name_1 = "Karuna"
# name_2 = ""

# if len(name_1)==0:
#     print("Length of string name_1 is 0")
# else:
#     print("Length of string name_1 is not equal to 0")

# if len(name_2)==0:
#     print("Length of string name_2 is 0")
# else:
#     print("Length of string name_2 is not equal to 0")

# name = " "
# print(repr(name))
# name ="Karunas"
# print(list(enumerate(name)))

# print("=================================================================")

# a = [1,2,3,4,5]
# print(range(3))
# print(list(range(3)))
# a.extend(range(3))
# print(a)
# print("=================================================================")
# print("Syntax for Functions")

# def add():
#     return "Hello"

# print(add())
# print("---------------------------------")
# def print_me():
#     print("I am here")

# print(print_me())

# print("---------------------------------")

# def sum(a,b):
#     total = a+b
#     return total

# #print(sum(4,6))

# total_amount = sum(4,6)
# print(total_amount)

# print("---------------------------------")

# def foo():
#     return "some_string"

# if foo():
#     print("print something")

# print("---------------------------------")

# def foo():
#     return ""
# if foo():
#     print("Print something")

# print("---------------------------------")

# def foo():
#     return None
# if not foo():
#     print("print something")
# print("---------------------------------")

# print("AND OPERATOR")

# print("AND - BAD - FIRST FALSE LAST TRUE")

# print(1 and 2 and 3 and 4)
# print(1 and 2 and 3)
# print(1 and 2 and 0 and 3)
# print(1 and 2 and [] and 4)
# print(1 and 2 and -3 and 4 and 5 and {})
# print(1 and {} and [] and 5 and 0)
# print(False and 0 and [] and None)

# print(2 and "Data Science")
# print(2 and " Datascience" and "AI")
# print(" " and "KS" and "")
# print(repr(" " and "KS" and ""))
# print(" " and "KS" and " ")
# print(repr(" " and "KS" and " "))

# print("The  repr() function returns a printable representation of the given project")

# print("---------------------------------")

# print("OR OPERATOR")

# print("OR - Good - First True last False")
# print(1 or 2)
# print(0 or 2)
# print(None or 5)
# print(False or 6)
# print(True or False)
# print(False or True)
# print([] or True)
# print([] or 0 or {})
# print([] or "ABC" or {22})
# print(None or None)
# print(0 or {} or [])
# print(0 or (10-10) or "BB")

# print([] or {} or 0)
# print([] or "ABC" or {22})
# print(False or False or True)

# print(None  or 0j or True)
# print(None or {} or 0j)

# print("---------------------------------")

# print(("Tamil" or "English")and ("England" or "Australia")) 
# print("Tamil" and "England")#first True in or , Last true in and
# print("---------------------------------")

# print("sir" and {False} and 56)
# print("sir" and False and 56)
# print("sir" and [False] and 56)
# print("sir" and (12) and (False) and 56)
# print("---------------------------------")
# print(True + True)
# print(True + False)
# print(False + False)
# #print(True + None)
# print("=================================================================")

# print("LAZY EVALUATION")


#  def add(a, b):
#     return a + b

# result = add(5, 10)
# print(result)
# print(add(result, 20))
# print("-----------------------------------------")
# def print_me():
#     print("I am here")

# print(1 or print_me())
# print(print_me() or 1)
# print(1 and 2 and print_me() and 5)

# print("-------------------------------------------")
# def print_me():
#     print("I am here")
#     return False

# print(1 or print_me())
# print(print_me() or 1)
# print(1 and 2 and print_me() and 5)

# print("-------------------------------------------")

# print("Testing for Multiple condition")
# a = 1 
# b = 6
# if a and b>1:
#     print("Yes")
# else:
#     print("No")

# print("======================================")

# if (a>2) and (b>1):
#     print("yes")
# else:
#     print("No")

# print("=======================================")

# a =1

# if (a==3) or 4 or 6:
#     print("yes")
# else:
#     print("No")
# print("=================================================================")

# a = 1

# if (a==3) or (a==4) or (a==6):
#     print("Yes")
# else:
#     print("No")

# print("=================================================================")

# a = 1

# if (a==1) or (a==4) and a(a==6):
#     print("Ravi")

# else:
#     print("No")

# print("=================================================================")

# print(True or False and False)  #Logical precedence (NOT>>AND>>OR)

# print("=================================================================")

# a = 1

# if a not in [3,5,6]:
#     print("Yes")
# else:
#     print("No")

# print("=================================================================")

#None

# marks = None

# if marks is None:
#     marks=35
# print(marks) #This is pythonic way of checking if an object has an value or not.

# print("=================================================================")

# import datetime

# aDate = None

# if aDate is None:
#     aDate=datetime.datetime.now()

# print(aDate)

# print("=================================================================")

print("Keywords we seen today-- is,in,not,None,True,False,and,or,if,else,elif,pass,def")

import keyword
print(keyword.kwlist)
print("The length of keywords:",len(keyword.kwlist))
print("=================================================================")

def add(a,b):
    print("The value of a:",a)
    print("The value of b:",b)
    if a:   
        return a
    else:
        return b
    
result = add(0,4)
print(result)
print("=================================================================")
