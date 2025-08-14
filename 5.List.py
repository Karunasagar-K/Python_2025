# #List(Collection data types)

# a =["a",1,"Python",(1,2),{}]

# print(a)
# print("Type:",type(a))
# print("Id of list a:",id(a))
# print("Id of item Python is:",id(a[2]))
# print("======================================================================")

# a[2]="Java"
# print(a)
# print("Id of list a:",id(a))
# print("Id of item Java in list a is:",id(a[2]))
# print("Length of list a is",len(a))

# print("=========================================================================")
# #Index

# #Positive index- starts from 0(left to right)
# #Negative index - starts from -1(right to left)

# print(list(range(30))) 


# print("=================================================================================================")
# sports = ["Handball","Cricket","Volleyball","Hockey","Tennis","Kabadi","Basket Ball","Football","KhoKho"]
# print("No of items in the sports list:",len(sports))
# print("ID of list sports is:",id(sports))

# #To know the index number
# for i in enumerate(sports):
#     print(list(i))

# #Range of index
# print(sports[2:5])  #Positive slice
# print(sports[:])     
# print(sports[4:4])
# print(sports[3:3])
# print(sports[4:2])

# print('negative slice',sports[-4:-1-1]) #Negative Slice


# print(sports[1::4]) #It will print the alternate items starts from Cricket which is 1st index mentioned in code.4 is step.



# thelist=["apple","apple","banana","banana","cherry","nectar","Halwa","Apple"]

# print(id(thelist))

# for i in thelist:
#     print("item:",i,"item's id:",id(i))

# #Duplicate items shares same id

# if "banana" not in thelist:
#     print("Banana is in thelist")
# else:
#     print("Banana is Not in thelist")
# print("==============================================================")


# """
# INDEXING:
# 1.Indexing is used to retrive a single element from a sequence.
# 2.The indexing operator in python is the python brackets([]).
# 3.Indices start from "0" for the first element and negative indices can be used to access elements from the end of the sequence.
# 4.To index the element, you specify the index position within the square brackets.
# 5.The result of indexing is the individual element at the specified index


# SLICING:
# 1.Slicing is used to extract the portion of a sequence.
# 2.The slicing index in python is start:step:stop 
# 3.where start is the index to start the slice(inclusive),stop is the index to end the slice(exclusive),step is optional step size for selecting elements.
# 4.Slicing returns a new sublist containing the selected elements.
# 5.If start is not sepecified,it defaults to the beginning of sequence.
# 6.If stop is not specified, it defaults to the end of the sequence.
# 7.If step is not specified, it defaults to 1. 
# """

# #List Function/Methods and supported operators:

# #Append -Add an elements to end of the list
# #clear  -Remove all the items/elements in the list
# #copy   -Returns the copy of the list
# #count  -Returns the number of elements/items in the list
# #extend -Add the elements of list(any iterable)to emd of the current list
# #insert -Add an item/element at speciific position
# #index  -Returns the index of the first elements of specified value
# #remove -Removes the first item with specified value
# #pop    -Removes the element with specified position
# #reverse-Reverse the order of the list
# #sort   -sort the list

# print("=================================================================")

# #1.Append(value)

# a = [1,2,3,4,5]
# print(a)
# print(id(a))
# print(type(a))
# print("=====================================")
# a.append(6)
# a.append(7)
# print(a)
# a.append([8,9])
# print(a)

# a.append(list(range(10,13)))
# print(a)
# print(id(a))

# print(help(list.append))

# for i in enumerate(a):
#     print(i)


# print(a[7])
# print(a[7][0])
# print(a[7][1])


# print("========================================================")

# #2.insert(index,value)
# print("INSERT")
# thelist = ['apple','banana','cherry']

# print(id(thelist))
# print(type(thelist))

# thelist.insert(1,"orange")
# thelist.insert(2,"orange")

# print(thelist)
# print(id(thelist))

# print("================================================================")

# #3.Remove(value)
# print("REMOVE")
# print(thelist)

# thelist.remove('orange')

# print(thelist)

# print(help(list.remove))

# print("====================================================================")

# #4.pop[Index])

# #LIFO/FIFO/STACK/NIFO(next in first out)

# a = [1,2,3,4,5,6,7,7,8,9,10]

# a.pop()

# print(a)

# a.pop(0)

# print(a)

# print(help(list.pop))

# print("=================================================================")

# a= ['apple','banana','cherry']

# print(a[1])

# del a[0]

# print(a)
# print("=================================================================")

# #del()-removes the specified index

# a=list(range(10))
# print(a)

# del a[::1]
# print(a)

# print("==============================================================")

# #5.Index(value,[StartIndex])
# a= [10,20,30,40,50,60,60,70,60,8,0,"GBU"]
# print(a)

# for i in enumerate(a):
#     print(i)
# print(a.index(0))
# print(a.index(60))
# print(a.index(60,6,11))


# print("=================================================================")
# #6.list.Clear()

# print("List.clear()")

# a = ["apple","banana","cherry"]

# print(a)
# print(id(a))
# print(type(a))

# print(a.clear())
# print(a)
# print(id(a))

# print("=================================================================")

# #6.list.reverse()

# print("list.reverse()")
# a = [1,2,3,4,5,6,"AAA"]
# print("Before reverse:",a)
# print(id(a))
# print(type(a))
# for i in a:
#     print(i,id(i))

# a.reverse()
# print("After reverse:",a)
# print(id(a))
# for i in a:
#     print(i,id(i))
# print("=================================================================")
# #Another method of reversing

# a = [1,2,3,4,5,6,"AAA"]
# print(id(a))
# print("Another method of reverse:",a[::-1])
# print(id(a))

# print("=================================================================")
# #7.count(value)
# a = [10,5,69,48,75,5,42,36,"AAA","BBB","CCC","AAA"]

# print(a.count(5))
# print(a.count("AAA"))
# print(a.count(48))



# print("=================================================================")
# #8.sort(key,reverse)


# a = [50,60,80,40,30,20,70,90,10,100,250,500,1,10,1000]
# print(a)
# a.sort()
# print("After sort in acending order:",a)

# a = [50,60,80,40,30,20,70,90,10,100,250,500,1,10,1000]
# a.sort(reverse=True)
# print("After sort in decending order",a)

# a = ["Sara","Karuna","Abi","AAthi","Aadhitya","m","g","k","z","Z","U","Y"]

# # for i in a:
# #     print(i,ord(i)) #Note:ord(i) only works on single characters, not strings.
# #                     #Since some elements in 'a' are names or multi-character strings, your code will throw an error.

# a.sort() #lexicographical order based on ASCII
# print(a)

# print("=================================================================")
# #9.copy

# #copy using assignment operator

# org_list = ["Karuna","Senthil","Kamesh"]

# my_list = org_list #copying the original list asignment operator

# print("Original list:",org_list)

# org_list.append("Shyam")

# print("Modified original list:",org_list)

# print("copied list:",my_list)


# print(id(org_list))
# print(id(my_list))

# '''
# * Id of original list and copied list using OPERATOR is remains same.
# * Changes made in original list will automatically also be made in copied list '''
# print("=================================================================")
# #copy using list()

# list1 = ["Honda","Yamaha","Maruti"]

# print("Original List:",list1)
# print("Original List ID:",id(list1))

# list2 = list(list1)

# print("Copied List:",list2)
# print("Copied List ID:",id(list2))

# list1.append("Hero")
# print("Modified List:",list1)
# print("Modified List ID:",id(list1))

# print("Copied List:",list2)
# print("Copied List ID:",id(list2))


# '''
# * Id is dfifferent from list1 and list2
# * list1 is different from list2. 
# * Changes made in list1 is not reflected in list2.
# '''
# print("=================================================================")

# #Copy using copy() method: list2 = list1.copy()

# o_list = ["Bike","mobile","Laptop"]

# print("Original list:",o_list)
# print("Original list ID:",id(o_list))

# o_list.append("Watch")

# m_list = o_list.copy()

# print("Modified list:",m_list)
# print("Modified list ID:",id(m_list))

# m_list.append("Car")

# print("Modified list:",m_list)
# print("Modified list ID:",id(m_list))

# print(o_list)

# print("=================================================================")
# o_list.append("Shoe")

# print("Original list:",o_list)
# print("Original list ID:",id(o_list))

# print("Modified list:",m_list)
# print("Modified list ID:",id(m_list))

# ''' In list.copy() method
# * list1 is different from list2. 
# * Changes made in list1 is not reflected in list2.
# * Id of both list are different
# '''

# print("=================================================================")
# print("Joining the two strings")

# a = ['karuna','Naveen','Karthi']
# b = [1,2,3,]

# print("Id of list a",id(a))
# print("Id of list b",id(b))
# c = a+b
# print(c)
# print("Id of list c",id(c))
# print("=================================================================")
# print("join using extend method")

# a = ['Ganga','Ritu','Kavi']
# b = ['Hema','Bagya','Thuvi']
# print("list1",a)
# print('list2',b)

# print("Id of list a",id(a))
# print("Id of list b",id(b))

# a.extend(b)
# print("list1",a)
# print('list2',b)
# print("Id of list a",id(a))
# print("Id of list b",id(b))

# print("=================================================================")

# t = []

# print(t)

# t.append("Karuna")
# print(t)

# t.append("Kamesh")
# print(t)

# t.extend(["Senthil","Rahul","Vipin"])
# print(t)

# print("=================================================================")

# #Using list() constructor


# thislist =list(("Apple","Banana","Cherry"))
# print(thislist)
# print(id(thislist))
# print(type(thislist))
# print("=================================================================")

# #Multiplying an existing list
# '''Note : multiplying an existing list by an integer will produce a larger list consisting of 
# that many copies of the original. This can be useful for example for list initialization:'''

# lst = [450, "Name", True] 
# print (lst * 3) 
# lst1 = [1, 2, 3, 4, 5] 
# print (lst1 * 5) 

# print("=================================================================")
# '''
# There are 5 ways of copying 
# 1.using assignment operator // lst2 =lst1. Already covered. Refer page no 69 
# 2. using list() // list(list1) 
# 3.using copy()//(import copy package) 
# 4. using deepcopy() //(import copy package) 
# 5. using slicing //b = a[:] '''

# print("=================================================================")
# Type-1
# ''' copy using assignment operator 
# the change made in the copied list is reflected on original list
# id() of original list and mylist() are same.
# '''

# print("=================================================================")

# import copy

# original_list = [10,20,3,["Lin","Mel"]]
# print("Original_List:",original_list)
# print("Id of the Original_list:",id(original_list))

# for i in original_list:
#     print(id(i))

# print("=================================================================")
# duplicate_list = copy.copy(original_list)
# print("Duplicate list:",duplicate_list)
# print("Id of the Duplicate_list:",id(duplicate_list))

# print("=================================================================")
# for i in duplicate_list:
#      print(id(i))

# duplicate_list.append(1000)
# print("=================================================================")

# print("Original list after copying and adding element",original_list)
# print("Duplicate list after copying and adding element",duplicate_list)

# print("=================================================================")
# print("Id of the Original_list:",id(original_list))
# print("Original list after copying and adding element",id(original_list))  
# print("Id of the Duplicate_list:",id(duplicate_list))
# print("Duplicate list after copying and adding element",id(duplicate_list))

# print("=================================================================")

# print("Original List(before copy):",original_list)
# duplicate_list =copy.copy(original_list)
# print("Duplicate List(After copy):",duplicate_list)

# print("---------------------------------")

# print("Id of original list:",id(original_list))
# print("Id of duplicate list:",id(duplicate_list))

# print("---------------------------------")

# for item in original_list:
#     print("Id of each element in the original list:",id(item))

# print("---------------------------------")

# for item in duplicate_list:
#     print("Id of each element in the duplicate list",id(item))
# print("---------------------------------")

# duplicate_list[3][1]= 'change'

# print("Original List(after updating duplicate list):",original_list)
# print("Duplicate List(After updatinf an element within nested list):",duplicate_list)

# print("---------------------------------")

# print("Id of original list(After updation):",id(original_list))
# print("Id of duplicate list(After updation):",id(duplicate_list))

# print("---------------------------------")

# for i in original_list:
#     print("Id of each element in original list",id(i))

# print("---------------------------------")

# for i in duplicate_list:
#     print("Id of each element in duplicate list",id(i))

# '''From my understanding Shallow copy means
# * The copy module provides the function copy.copy() which creates the shallow copyof the object.
# * A shallow copy creates a new object, but the content is still referred to the original object.
# * So if the original object contains mutabke objects(e.g list, dict)changes made to these copied object will be reflected in original object as well.
#   '''
# print("=================================================================")

# print("Deep copy")

# '''
# Copy using deepcopy() method the change made in the list did not effect in other lists.
# '''

# import copy

# original_list =  [90,80,75,["Susi","Mani"]]
# print("Original list",original_list)
# print("Id of original list:",id(original_list))

# for i in original_list:
#     print("Id of each element in original list",id(i))

# print("---------------------------------")

# duplicate_list = copy.deepcopy(original_list)
# print("Duplicate list:",duplicate_list)
# print("Id of Duplicate list:",id(duplicate_list))

# for i in duplicate_list:
#     print("Id of each elemnet in duplicate list",id(duplicate_list))

# print("---------------------------------")

# duplicate_list.append(1000)

# print("Original list after copying and adding the new elemnet",original_list)
# print("Dupliicate list after copying and adding the new element",duplicate_list)
# print("---------------------------------")

# print("Id of original list",id(original_list))
# print("Id of original list after copying and adding new element",id(original_list))
# print("Id of Duplicate list",id(duplicate_list))
# print("Id of duplicate  list after copying and adding new element",id(duplicate_list))

# '''
# * The copy module also provide function copy.deepcopy() which creates a deep copy of a object.
# * A deep copy creates a object completely independent copy of an object and it content.
# * Any changes made to the elements in copied object will not affect the original object. 
# '''

# print("=================================================================")

# print("b=a[:]--- Alternative to list.copy()")

# a = [1,3,"Youva","TRU","FA"]
# print("Original list",a)
# print("Id of list a",id(a))

# b = a[:]

# print(b)
# print("---------------------------------")

# b.append("kamaraj")

# print("list b after append:",b)
# print("list of a after append:",a)
# print("ID of list b:",id(b))
# print("Id of list a",id(a))

# '''
# Changes made in list b does not reflected in list a '''

# print("=================================================================")
