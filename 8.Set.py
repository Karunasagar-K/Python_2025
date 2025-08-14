# set1 = {1,2,3}
# set2 = set()
# set3 = {}
# print(type(set1))
# print(type(set2))
# print(type(set3))

# print("=================================================================")

# myset = {"apple","banana","cherry"}

# print(myset)
# print(type(myset))
# print(id(myset))

# print("=================================================================")

# print("Python has a set of build in methods that you can use on sets")

# add()   - Adds an element to the set
# clear() - Removes all the elements from the set
# copy()  - Returns the copy of the set
# difference() - Returns a set that containing the difference b/w two or more sets
# difference_update() - Removes the item in the set that are also included in another,specified set.
# discard() - Removes the specified item
# intersection() - Returns a set, that is the intersection of two other sets
# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() - Returns whether two sets have a intersection or not
# issubset() - Returns whether another set contains this set or not
# issuperset () - Returns whether this set contains another set or not
# pop() - Remove the element from the set
# remove() - Removes the sepecified element
# symmetric_difference() - Returns a set with symmetric differenece of two sets
# symmetric_difference_update() - Inserts the symmetric differences from this set and another.
# union() - Return a set containing the union of sets.
# update() - Update the set with union of this set and others.

# print("Mutable vs Immutable")

# '''Mutable - can be edit - Aadhar card number,bank acc number
#    Immutable -cannot be edit -phone number
# '''

# print("=================================================================")

# bank = "STATE BANK OF INDIA"
# print(bank)
# print(type(bank))
# print(id(bank))
# print(len(bank))

# #Conert into the set
# result = set("STATE BANK OF INIDA")
# print(result)
# print(type(result))
# print(id(result))
# print(len(result))

# #Set allows only unique values
# print("=================================================================")
# #Add ()

# a ='hello'
# a = set(a)
# print(a)
# print(type(a))

# a.add(6) #We add one element at a time 
# print(a)
# print("=================================================================")
# #Update()

# a = {'A',"B","C"}
# b = {1,2,3}
# a.update(b) #use this method 
# print(a)

# #a=a.update(b) -Dont use this method,it returns null value
# print("=================================================================")

# #Update a set with set

# a = {"A","B","C"}
# b = {3.5,"KL",45}

# a.update(b) #Set automatically removes the duplicate values and do not preserve order
# print(a)
# print("=================================================================")

# #Update a set with list

# a = {'A','B','C'}
# b = [10,20,30,'vikki']

# a.update(b) #Always use this type of update,it does up mix and match
# print(a)

# print("=================================================================")

# # We can update multiple sets using update()

# a ={"A","B","C"}
# print(id(a))
# b ={10,20,30,'vikki'}
# print(id(b))
# c ={'Mani',"Pandi"}
# print(id(c))
# d ={10,10000}
# print(id(d))

# a.update(b,c,d)
# print(a)
# print(id(a))
# print("=================================================================")

# #Union()/operator'|'

# '''
# a.union(b) or a|b returns the new set(new id), from both sets, but duplicate will be removed.
# Return the union of the sets of a new set. i.e all elements that are in either set.

# '''


# a ={"A","B","C"}
# print(id(a))
# b ={10,20,30,'vikki'}
# print(id(b))

# #a = a|b 
# a = a.union(b)
# print(a)
# print(id(a))

# print("=================================================================")

# #Intersection()/Operator '&'

# '''
# a.intersection(b) returns a new set / common values from both set
# '''


# a = {1,2,3,4}
# print(id(a))
# b = {3,4,5,6}
# print(id(b))

# a =a.intersection(b)
# print(id(a))

# print(a)
# print("=================================================================")

# #Intersection_Update()
# '''
# The  method modifies the original set by keeping only the elements that are common between itself and one or more other sets.
# '''

# a = {"A","B","C","D","E",5,7}
# print(id(a))

# b = {"A","B","C","V",5,"P"}
# print(id(b))

# a.intersection_update(b)
# print(a)
# print(id(a))

# print("=================================================================")

# print("POP")

# a = {"A","B","C"}
# b = a.pop()

# print(b)
# print(a)
# print("=================================================================")

# print("Remove")

# '''Removes the specified element'''

# a ={"A","B","C"}
# a.remove("A")
# print(a)

# print("=================================================================")

# #Raises key error if we want to remove a non exisiting item from the set 
# a = {'A', 'B', 'C'} 
# a.remove('E') 
# print (a)

# print("=================================================================")
# a = {"A","B","C"}
# b = {10,20,30}
# b = a.copy()
# print(b)

# a.remove("C")
# print(a)
# b = a.copy()
# print(b)

# print("=================================================================")

# a = {"A","B","C"}
# b = {3.5,"KL",45}

# a.clear()
# print(a)

# print("=================================================================")
# print("Difference()/operator'-'")
# '''
# The difference() method returns a set that contains the difference between two sets.
# The returned set contains items that exist only in the first set, and not in both sets.
# '''
# a = {1, 2, 3}
# b = {3, 4, 5}

# a = a.difference(b)

# print(a)

# print("=================================================================")
# a = {'A', 'B', 'C', 'D',10} 
# print("LENGTH of set a BEFORE  difference update ", len(a)) 
# b = {'A', 'B', 'C', 'D', 'E'} 
# c = {'A',10, 'C',200, 300}

# #print(a.difference(b,c)) #  possible 
# d = a.difference(b,c) 

# print(d)

# print("=================================================================")

# print("Difference update")
# '''
# The difference_update() method removes the items that exist in both 
# sets. The difference_update() method is different from the 
# difference() method, because the difference() method returns a new 
# set, without the unwanted items, and the difference_update() method 
# removes the unwanted items from the original set. 
# '''
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# a.difference_update(b)
# print(a)  # Output: {1, 2}

# print("=================================================================")
# a = {'A', 'B', 'C', 10,20} 
# print("id of a ", id(a)) 
# print("LENGTH of set a BEFORE  difference update ", len(a)) 
# b = {'A', 'B', 'C', 'D', 'E'}
# c = {'A', 'B', 'C',200, 300, 10}

# a.difference_update(b,c) # d = a.difference_update(b,c) NOT possible 
# print(a) 
# print("id of a ", id(a)) 
# print("==========") 
# print("After diffence_update(), the unique values in set a is  retained", a) 
# print("LENGTH of sete a AFTER difference update ", len(a)) 
# print(b) 
# print(c)

# print("=================================================================")


# print("Symmetry_difference / Operator'^'")

# '''
# a.symmetry_difference(b) - returns a new set by removes the common items in both the sets.
# '''
# a = {'A', 'B', 'C', 10,20} #checks both sets 
# b = {'A', 'B', 'C', 'D', 'E',} #checks both sets

# print("ID of set A before SYMMETRIC_DIFFERENCE() is", id(a)) 
# print("ID of set b before SYMMETRIC_DIFFERENCE() is", id(b)) 
# c = b.symmetric_difference(a) 
# print(c)

# print("set a values", a) 
# print("set b values", b) 
# print("ID of set c after SYMMETRIC_DIFFERENCE() is", id(c))

# print('=' *50) 

# print("SYMMETRIC_DIFFERENCE_UPDATE() / operator(^=)")
# '''
# This method is used to return the symmetric difference of a set and the set of elements 
# from the iterable like string, list, set passed as an argument. It is very similar to 
# symmetric_difference() method, with difference is that where symmetric_difference() 
# method create and return a new set. 
# symmetric_difference_update() method updates the set on which this method is 
# invoked, the id of the original set will not be changed 
# '''

# a = {'A', 'B', 'C', 10,20} #checks both sets 
# b = {'A', 'B', 'C', 'D', 'E',} #checks both sets 
# a.symmetric_difference_update(b) 
# print("SET a is", a) 
# print("SET b is", b) # common value are A,B,C are gone 
# print("LEN AFTER difference", len(a) )

# print('=' *50) 

# print("Subset and superset(a<=b,a>=b)")
# '''
# In mathematics, a set A is a subset of a set B if all elements of A are also elements 
# of B;  
# B is then a superset of A. It is possible for A and B to be equal; if they are unequal, 
# then A is a proper subset of B. ... The subset relation defines a partial order on 
# sets.

# '''


# a = {'A', 'B', 'C', 10,20} 
# b = {'A', 'B', 'C', 'D', 'E',10,20}

# print(a.issubset(b)) 
# print(b.issuperset(a)) 

# #a.issubset(b) tests whether each element of a is in b. 
# #b.issuperset(a) tests whether each element of a is in b.

# print("="*70)

# a = {'A', 'B', 'C', 11,20} 
# b = {'A', 'B', 'C', 'D', 'E',10,20} 
# print(a.issubset(b)) 
# print(b.issuperset(a))

# print("="*70)

# B = {1, 2, 3} 
# C = {1, 2, 3}

# print(B.issubset(C))
# print(C.issubset(B))
# print(B.issuperset(C))
# print(C.issuperset(B))

# print("="*70)

# print("Disjoint sets")
# '''
# The isdisjoint() method returns True if none of the items are present in both 
# sets, otherwise it returns False. '''

# B = {10, 20, 30} 
# C = {1, 2, 3} 
# print(B.isdisjoint(C)) 
# print(C.isdisjoint(B)) 

# print('=' *50) 
# print("Testing membership in set") 
# print("The builtin in keyword searches for occurances") 
# B = {10, 20, 30} 
# print(20 in B) 
# print(2 in B)

# '''
# Set is unorderd,immutable, does not support indexing,unique.
# '''

# names = {"Adam","Beth","Charlie"}

# my_list = [1,2,3]
# my_set = set(my_list)

# print(type(my_list))
# print(type(my_set))

# if "Adam" in names :
#     print(True)


# setA = {"CCC","BBBB","AAAAA"} 

# for idx, item in enumerate(setA):
#     print(idx,item)

# print("Frozenset")

# '''
# frozenset() Parameters 
# The frozenset() function takes a single parameter: 
# * iterable (Optional) - the iterable which contains elements to initialize the 
# frozenset with. 
# * Iterable can be set, dictionary, tuple, etc. 
# ie, any mutable object can be converted into immutable using frozenset 
# (To add an element to a frozenset , first convert the frozenset to a list, then 
# append) // 
# '''

# set = {10, 20, 20, "AA", "BB", "CC"} 
# dic = {10:"Ten", 20:"Twenty", 30:"Thirty", "AA":"aa"} 
# lst = [10, 20, 20, "AA", "BB"]


# print(type(set))
# print(type(dic))
# print(type(lst))

# hset = frozenset(set)
# print(hash(hset))

# print("="*70)

# #Converting the dictionary into frozen set,gives only the keys not the values.
# frozendic = frozenset(dic)
# print(dic)
# print(frozendic)
# print(hash(frozendic))
# print("="*70)

# #Converting the lst into frozen list
# frozenlist = frozenset(lst)
# print(lst)
# print(frozenlist)
# print(hash(frozenlist))


# # Now i need to add an element to that frozenlst, in frozen list i cant do that, so i am converting the frozen list into normal list.

# lst = list(frozenlist)
# print(lst)
# lst.append("ZZZZ")
# print(lst)

# frozenlist = frozenset(lst)
# print(lst)
# print(frozenlist)

# print("="*70)

# print("Return value from frozenset()")

# print(frozenset(set()))

# print(frozenset("KARUNA"))

# vowels = ("a","e","i","o","u")

# print(type(vowels))

# fset = frozenset(vowels)
# print(fset)

# #fset.add("h") #not possible

# print(type(fset))

# for i in fset:
#     if i=="a":
#         print(f"{i} is a vowel")
#     else:
#         print(f"{i} is a constant")
# print("="*70)

text = "A paragraph is a short collection of well-organized sentences which revolve around a " \
"single theme and is coherent. " \
"A good paragraph expresses everything it has to say briefly."
vowels = ('a','e','i','o','u')


# for i in text:
#    if i.lower() in vowels:
#       print(f"{i} is vowel")
#    else:
#       print(f"{i} is not a vowel")

# print("="*70)
# vowel = 0
# constant = 0

# for i in text:
#     if i.isalpha():
#         if i.lower() in vowels:
#             vowel = vowel+1
#         else:
#             constant = constant +1

# print(f"There are {vowel} vowels")
# print("="*70)
# print("Discard")

# '''Discard - No error is given if try to remove non existing item'''

# set = {"Karuna","Naveen","Kayal",10,250,38,5.5}
# print(set)
# print(id(set))
# print(type(set))
# set.discard("JU")
# print(set)  # No error is showing even if we try to discard an item which is not available in the set.
# set.discard("Karuna")
# print(set)
# print("===========================================================================")

# print("Remove")
# ''' Remove() SHOWS  ERROR if we try to remove an item/element which is not available in the set '''
# set = {"Karuna","Naveen","Kayal",10,250,38,5.5}
# print(set)
# set.remove("Kayal")
# print(set)

# print("===========================================================================")


# set1 = set()
# set1.add(5)
# print(set1)

# print("===========================================================================")

# set1 = set()
# set1.add( () )
# print(set1)

# print("===========================================================================")

# set1 =set()
# set1.add( []) #TypeError: unhashable type: 'list' 
# print(set1)
# Only hashable elements can be added to a set.[] is unhashable

# print("===========================================================================")


# print("=============== Update ================")
# set = {10, 20, 20, "AA", "BB", "CC"} 
# print(set) 

# set.update("H")
# print(set)

# print(set) 

# set.update(["Poonusamy"])
# print(set)

# set.update("MMMM") #It does allow duplicate values
# set.update("Lollu")
# print(set)
# # To add string as a whole wrap it in a tuple or list

# print("===========================================================================")

# print("Get the unique elements of a list using set")

# lst = [10,20,30,20,10,50,60,60,"Karuna","Karuna","Naveen","Funny"]
# print(len(lst))
# print(type(lst))


# b =set(lst)
# print(b)
# print(type(b))
# print(len(b))
# print("===========================================================================")

# list1 = list("We are learning and DS")
# print(len(list1))
# print(type(list1))

# b = set(tuple(list1)) 
# print(b)
# print("===========================================================================")
# bankCustomers = {'Gomathi', "Anto", "Emalta", "Kamal", "Gomathi", "Mahesh", "Usha", 
# "Kamal", "Viji", "Usha", "Nithya", "Nithya""Nithya"} 
# print (bankCustomers) 
# print(len(bankCustomers))

# '''
# Sets are unordered collections of distinct elements. But sometimes we want to 
# work with unordered collections of elements that are not necessarily distinct and 
# keep track of the elements' multiplicities. 
# '''
# print("===========================================================================")
# print("usha" in bankCustomers)

from collections import Counter 
bankCustomers = ["Gomathi", "Anto", "Emalta", "Kamal", "Gomathi", "Mahesh", "Usha", 
"Kamal", "Viji", "Usha", "Nithya", "Nithya","Nithya"] 
print(bankCustomers) 
print(len(bankCustomers))

print("===========================================================================")
set1 = set(bankCustomers) 
print(set1) 
print(len(set1))

print("=======================================================================") 
b =  Counter(bankCustomers) 
print(b)

print("===========================================================================")
#Convert the frozenset to set vice versa 
a={'A','B','C',10,20} 
aF=frozenset(a) 
aS=set(aF) 
print(aF)
print(type(aF)) 
print(aS) 
print(type(aS)) 
print("===========================================================================")

c1 = Counter()                                           
print(c1) 
print(type(c1))
print("==================================================================") 

c2 = Counter("Karunasagar")
print(c2)
print(type(c2))

print("===========================================================================")
c3 = Counter( {'a': 4, 'b': 2} )           
print(c3) 
print("================================================================") 

c4 = Counter(age = 205, Marks = 95, Zebra = 1000)                                                
print(c4)  # the output is in desending order based values 
print("==================================================================")

a = Counter(['H', 'E', 'L', 'L', 'O', "Lara", 10, 20, 10, "Lara"]) 
print(a)

'''
* Output is lokk like Dict.
* Counter is a dictionary where elements are stored as dictionary keys and their counts are stored as dictionary values.
'''



print("===========================================================================")