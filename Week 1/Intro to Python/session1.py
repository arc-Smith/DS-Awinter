# CRASH COURSE

############### [LISTS]

    # don't have to specify int or strings or etc
    # LISTS in Python is pretty much an ArrayList
# a = [10,12,15,16,18]
# # a.append(6) # add a 6 to the end
# # a.pop() # remove from the end
# # a.insert(0, 100)
# # a.sort()
# print(a)

############### [LOOPS]

# Using RANGE:
# range (start, end, step)
# range(start=0, end, step=1)
# range(start, end, step=1) if we did (2,5) it'll go from 2->4
# 0 -> 4
#    [1, 2, 3, 4, 5, 100]
# i = 0  1  2  3  4   5
# for i in range(0, 5): # (start=0, end=5, step=1) this means starting at 0 going all the way to 5 (but NOT INCLUDING 5) taking steps of 1
#     # i=0
#     # i=1
#     # i=2
#     # i=3
#     # i=4
#     print("i:",i) # this is just providing a value from the iterator i. Gives us the index.
#     print("a[i]:",a[i]) # this is grabbing a value from the array a. Gives us the value at that index of a.
# for i in range(0, 100):
#     print("a[i]:", a[i]) # a ONLY has from 0-4 so if we try to locate a[5] we get IndexError
# characters = ["Gon", "Yuji", "Gojo", "Megumi"]
#             #   0       1       2        3
# # use len method if you do not know the exact length of data structure
# for i in range(0, len(characters)): # (start=0, end=4, step=1) with the range 0->3
#     print(characters[i])

# Using for each (calm)
# characters = ["Gon", "Yuji", "Gojo", "Megumi"]
# for c in characters:
#     print(c)

# Using enumeration method
# characters = ["Gon", "Yuji", "Gojo", "Megumi"]
# for i,char in enumerate(characters):
#     print(i)
#     print(char)

############### [FUNCTIONS]
# method creation
# def function1():
#     print("1")
# function1()

# passing by reference VS passing by value
# def printingElements(arr):
#     # passing in the actual array a
#     arr.append("Submarine")
#     print("INSIDE FUNCTION:", arr)

# arr = ["Car", "Airplane", "Bus"]
# printingElements(arr) # passing in an ADDRESS not just a VALUE
# print("OUTSIDE FUNCTION:", arr)

# INSIDE FUNCTION: ["Car", "Airplane", "Bus", "Submarine"]
# OUTSIDE FUNCTION: ["Car", "Airplane", "Bus", "Submarine"]

# def addTwo(one, two):
#     # passing in copies of two integers. Passing-by-value
#     # var1 = one
#     # var2 = two
#     print("INSIDE FUNCTION (what happens when calling addTwo):", one + two)


# one,two = 1,1

# addTwo(one, two) # passing in a VALUE not a whole ADDRESS

# print("OUTSIDE FUNCTION:", one + two)

# Tolani's Prediction:
# INSIDE FUNCTION: 2
# OUTSIDE FUNCTION: 2

############### [STRINGS]
# name = "john Doe"

# # for i in range(len(name)):
# #     print(name[i])

# # for c in name:
# #     print(c)

# print(name.capitalize())

# number = "00000200"
# print(number.lstrip("0"))

# # an alphanumeric char/number is just within one of these groups 0-9, a-z, A-Z
# char = "d"
# print(char.isalnum())

# print("Hello World!")

############### [DICTIONARIES]
# A pair. A key-value pair.
# Word -> definition for that word
# Key -> lock with information and whatnot

# dictionary = {}
# dictionary["Cap"] = "When someone is giving a clearly flawed and false statement about something"
# {"Cap":"When someone is giving a clearly flawed and false statement about something", ...}
# print(dictionary)

# for key,val in dictionary.items(): # [[all the keys], [all the values]]
#     print("KEY:", key)
#     print("VAL:", val)

# for key in dictionary.keys(): # [all the keys]
#     print("KEY:", key)

# for val in dictionary.values(): # [all the values]
#     print("VAL:", val)

# dictionary["Empty"] = None
# print(len(dictionary))
# print(dictionary["Empty"])

# Tuple (a list that can't be modified):
# (2, 2)
# (0, 0)
# tuple1 = (1, 2, 3, 4)

# List:
# [2, 2]

############### [CLASSES]
# look at the implementations of our data structures