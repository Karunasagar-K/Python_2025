# print("Loops")

# '''Loops enables the developers to set certain portions of their code to repeat through a number of times. '''

# print("Flowcontrol- The order of execution of the statements in a program is known as a flow of control.\nThe flow of control can be implemented using control structures.\n1.Selection\n2.Repetition")
# print("=================================================================")
# print("Infinite Loop")

# i=0
# while (i<7):
#     print(i) #Infinite

# print("=================================================================")

# print("Loop with Increment")

# marks = 0
# while marks<35:
#     print(marks)
#     marks=marks+5

# print("=================================================================")
# print("Break and continue")
# print("=================================================================")

# '''When a break statement executes inside a loop, control flow "breaks" out of the 
# loop immediately: 
# 1.break ==> when condition is met, it will break the entire loop and exit.
# 2.continue ==> when condition is met, it will just "SKIP REST of the statements within the 
# loop'''

# print("=================================================================")

# i = 0
# while i<7:
#     print(i)
#     if (i==4):
#         break
#     i = i+1

# print("=================================================================")

# for i in ("Karuna", 3,5,7,9, 6, "Senthil", "Kamesh", " ", False, "Senthil"): 
#     print((i)) 
#     if i == " ": 
#         break 
# print("=================================================================")

# marks = 35
# for name in ("Karuna","Ajith","Arun","Karthi","Vinoth"):
#     print(name)
#     if (name == "Karthi") and (marks >=35):
#         print(name,"mark  is",marks)
#         break

# print("=================================================================")

# a=0
# b=1
 
# while (a<6) and (b>8): # since b becomes FALSE, this while loop resturns FALSE, so the execution does not  go the next line 
#     print("a Value",a,"b Value",b)
#     a = a+1
#     b = b+1
# print("=================================================================")

# def test():
#     print("Canada")
#     break # break can not be used inside the fn to stop the fn execution, it is an error!

# print("=================================================================")

# for i in range(5):
#     test() # ie we call the fn in side the loop, so the fn can not be broken using break statement 

# print("=================================================================")

# for t in range(8):
#     print(t)
#     if (t==4):
#         break
#     else:
#         print("This Else  statement will bot be executed after 3rd execution")
# print("=================================================================")

# print("Continue Statement")

# '''It skips the current iteration and never comes out/terminate the loop. when condition is met, it will just "SKIP REST of the statements within the 
# loop "CONTINUE THE LOOP again. So in essence, "continue" should be called as "skip & continue" '''

# ''' A continue statement will skip to the next iteration of the loop bypassing the rest of the current block,but continuing the loop. As with break,conitunue also appears inside the loops'''
# print("=================================================================")

# lst = [2,4,6,8,10]
# for var in lst:
#     if (var==6):
#         continue
#     print(var)

# print("=================================================================")

# text = "KarunasagarGangadeviNagamuthuKaliyappanRithaniyaThuvitha"

# for letter in text:
#     if (letter=="K" or (letter=="g".lower())):
#         continue
#     print(letter,end="")
# print("=================================================================")
# lst = [2,4,6,8]
# for item in lst:
#     if item ==2:
#         break
#     print(item)

# #No output, because first conditiion itself it was satisfied and break the loop.Thats why there is no ouput.
# print("=================================================================")

# list_ =[2,4,6,8,10]

# for i in list_:
#     if (i== 4) or (i==8):
#         continue
#     print(i)

# print("=================================================================")

# print("Nested loops -How to use Loops?")

# r = 5

# for i in range(1,r+1):
#     for j in range (1,i+1):
#         print("*",end = " ")
#     print(" ")
# print("=================================================================")

# while True:
#     for i in range(1,5):
#         print(i)
#         if (i==2):
#             break  # This will break only the for loop not while loop. The while True loop restarts the for loop again from i = 1 → and the same cycle repeats forever, printing(1,2) 
#         break #breaks the  while loop

# print("=================================================================")

# a = 0
# while a<5:
#     for i in range(1,5):
#         print(i,a)
#         if(i==2):
#             break
#     a = a+1
# print("=================================================================")

# def m():
#     while True:
#         for i in range(1,5):
#             print(i)
#             if (i==2):
#                 return
            
# a = m()
# print(a)
# print("=================================================================")

# for d1 in range(6):
#     for d2 in range(6):
#         print(d1,d2)
# print("=================================================================")

# k=5

# for l in range(1,k):
#     for m in range(1,l+1):
#         print(m,end=" ")
#     print("")

# print("=================================================================")
# k=5
# for i in range(1,k):
#     for j in range(1,i):
#         print(j,end= " ")

# print("=================================================================")

# import random
# for i in range(100):
#     d1 = random.randrange(6)+1
#     d2 = random.randrange(6)+1
#     print(d1,d2,d1+d2)
    
# print("=================================================================")

# def breakloop():
#     for i in range(1,5):
#         if (i==3):
#             return i
#         print(i)
#     return

# a = breakloop()
# print(a)
# print("=================================================================")

# import random

# def odd(number): 
#     return number %2 !=0  #Odd function

# while True:  #Infinite loop untill we break
#     s = random.randrange(10) #For generatimg random number from 0 to 10

#     if (s==0):
#         print("zero")  
#         break  #loop stops when zero is found 
#     elif odd(s):
#         print(s,"Odd")
#     else:
#         print(s,"even")

# print("=================================================================")
# import random 

# def odd(number):
#     return (number %2 !=0)

# def report(number):
#     if (int(number)==0):
#         print("zero")
#         return
#     elif odd(int(number)):
#         print(number,"odd")
#         return
#     print(number,"even")
    
# def spinWheel():
#     t = random.randrange(38)
#     if (t==37):
#         return "00"
#     return str(t)

# def main():
#     for i in range(12):
#         n =spinWheel()
#         report(n)

# main()
# print("=================================================================")

# print("Enumerate")
# lst =["one","two","three","four"]

# for i in enumerate(lst):
#     print(i)
# else:
#     print("Executes after the completion of the for loop")

# print("=================================================================")

# for i in range (5):
#     print(i)
#     if (i==3):
#         print("HI")
#         break
# else:
#     print("After completion of the project")

# print("=================================================================")

# for i in range (5):
#     print(i)
#     if (i==3):
#         print("HI")
#         continue
# else:
#     print("After completion of the project")

# print("=================================================================")

# while False:
#     pass
# else:
#     print("Else clause will execute here")
# print("=================================================================")
# while True:
#     pass
# else:
#     print("Else clause will not execute,cos it is an indefinite loop")

# print("=================================================================")

# li = ['Sachin','shewag','Gambhir','kholi']

# for i in li:
#     if isinstance(i,int):
#         print("This is integer",i)
#         break
#     else:
#         print("This is string",i)
# else:
#     print("Only if list contains all string")

# print("=================================================================")

# lst = [3,"DS",5,'A', 89.4, 8,5] 
# for item in lst: 
#     if type(item) is not int: 
#         print(item)

# print("=================================================================")

# lst = [3,5,6,7,8,9]

# for i in lst:
#     if type(i) is not int:
#         print(i)
#         break
# else:
#     print("No exception")
    
# print("=================================================================")


# lst = [3,5,6,"D",8,9]

# for i in lst:
#     if type(i) is not int:
#         print(i)
#         break
#     else:
#         print(i)

# else:
#     print("No exception")

# print("=================================================================")

# print("The pass statement-useful as placholder for code is yet to  be written.")

# for x in range(10):
#     pass

# while True:
#     pass


# while x==y:
#     pass

# print("=================================================================")

# print("The half loop do while")

# a=10

# while True:
#     a = a-1
#     print(a)
#     if (a<7):
#         break
#     print("done")

# print("=================================================================")

# print("Looping and unpacking")

# collection = [('a','b','c'),('x','y','z'),('1','2','3')]

# for item in collection:
#     i1 = item[0]
#     i2 = item[1]
#     i3 = item[2]

#     print(i1,i2,i3)

# print("=================================================================")  
# lst = ['a','b','c','d','e','f']

# for s in lst:
#     print(s[:1],end=" ")
# print("=================================================================")

# lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo'] 
# for item in lst:
#     print(item) 
#     print(item[0:3])
# print("=================================================================")

# print("enumerate")
# for item in enumerate(lst):
#     print(item)

# print("=================================================================")

# lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

# for idx,i in enumerate(lst):
#     print(f"{i} has an index of {idx}")
# print("=================================================================")
# lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo'] 
# for index, item in enumerate(lst): 
#     print("item is ", item, "index is ", index) 

# print("=================================================================")

# lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']  #Remember python uses zero based indexing

# for i in range(len(lst)):
#     pass
# print(lst[2:4])
# print("=================================================================")

# for s in lst[1::2]:
#     print(s)

# for i in range(1,len(lst),2):
#     print(lst[i])
# print("=================================================================")
# print("Home work")

# while  True:
#     for i in range(1,5):
#         print(i)
#         if (i==3):
#             break
#     break

# print("=================================================================")

