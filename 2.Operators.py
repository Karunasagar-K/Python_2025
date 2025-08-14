# 1.Arithmatic Operators

internal_marks = 10
external_marks = 3
no_of_subjects = 5

print("Addition:",internal_marks + external_marks) #Add

print("Subraction:",internal_marks - external_marks) #Sub

print("Multiplication:",internal_marks * external_marks) #Mul

print("Division:",internal_marks / external_marks) #Div

print("Modulus:",internal_marks % external_marks) #Modulus

print("Exponential:",internal_marks ** external_marks) #Exponential

print("Floor division:",internal_marks // external_marks) #Floor_Division

# 2.Assignment Operator

#Assign : 

internal_marks = 15

print("Internal marks is:",internal_marks) 

#Add and Assign

a = 5
b = 3
print("a:",a)
# print("a+b:",a+b)

a +=5 #add
print("a+=5:", a)

a -=5 #sub
print("a-=5:", a)

a*=5 #mul
print("a*=5", a)

a/=5 #Div
print("a/=5", a)

a%=3 #Modulus
print("a%=5",a)

a//=2 #Floor Division
print("a//=2",a)

a=5
a**=3 #Exponential
print("a**=3",a)


# 3.Comparision Operator / Relational Operator

salary = 7500
bonus = 7400

print(salary != bonus)
print(salary <= bonus)
print(salary >= bonus)
print(salary == bonus)


# 4.Logical Operator
number = 50

print(number>10 and number<100)

print(number>150 or number<100)

print(not(number>10 and number<100))

# # 5.Identity Operator

a = 52640 #integer
b = 52640

c = "Karuna" #string
d = "Ganges"

e = [1,2,456] #List
f = [1,2,456]

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))

print(a is b)
print(c is d)
print(e is f)

# 6.Membership operators

my_list = ['Shewag','Sachin','Gauti','raina','yuvi','dhoni']

print("shewag" in my_list)
print("Shewag" in my_list)


  
