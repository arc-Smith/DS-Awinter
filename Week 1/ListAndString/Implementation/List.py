# REMOVE method
# listoffood = ["Hamburger", "Taco", "Pizza"]
# listoffood.remove("French Fries")
# print(listoffood)

# INDEX method
# listoffood = ["Hamburger", "Taco", "Pizza"]
# print(listoffood.index("Hamburger"))

# soulEaterChars = ["Kidd", "Star", "Maki"]
#                  #   0       1       2

# RANGE LOOP
# for i in range(len(soulEaterChars)):
#     print(soulEaterChars[i])

# FOR EACH LOOP
# for char in soulEaterChars:
#     print(char)

# WHILE LOOP
# i = 0
# while i < len(soulEaterChars):
#     print(soulEaterChars[i])
#     i += 1

# s = "Tolani"
#    0123456
# Printing "ni"
# print(s[4:])
# print(s[4:6])
# print(s[4:4+2])

# numList = [11, 14, 18]
# print(numList[0])
# print(numList[-3]) # accessing using negatives 
# stringList = ["Dasani", "Fuji", "Pure Aqua", "Poland Spring"] # O(1) time
# stringList.append("Essentia") # O(1) time
# stringList.insert(2, "Evian") # O(n) time
# print(stringList) # O(1) time
# stringList.insert(0, "Smart Water") # O(n) time
# print(stringList) # O(1) time

# arr = [1, 2, 3, 4, 5]
# arr.insert(5, 55)
# arr[self.size=5 - 4]









# stringList = [] # O(1) time

# # Insertion
# stringList.append("A") # O(1) time
# stringList.append("B") # O(1) time
# stringList.insert(2, "C") # O(n) time because of insertion at the beginning and needing to shift all n elements
# print(stringList) # O(1) time

# # Access
# print(stringList[2]) # O(1) time
# print(stringList[2]) # O(1) time

# # Traversal
# for i in range(len(stringList)): # O(n) time
#     print(stringList[i]) # O(1) time
# for char in stringList: # O(n) time
#     print(char) # O(1) time

# # Searching
# for char in stringList: # O(n) time
#     if char == "F": # O(1) time
#         print("The element is found") # O(1) time
#         break # O(1) time

# # Index of
# index = stringList.index("C") # O(n) time
# print("The element is found at index " + str(index)) # O(1) time

# # Remove
# stringList.remove("B") # O(n) time
# print(stringList)