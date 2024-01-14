# IMPORTS AND SETUP
from Implementations.SinglyLinkedList import SinglyLinkedList
from Implementations.SinglyLinkedList import SinglyNode
linkedlist = SinglyLinkedList(1)
linkedlist.insert_at_back(2)
linkedlist.insert_at_back(3)
linkedlist.insert_at_back(4)
arr2d = [[1,1,1], [2,2,2]]
arr1d = [2, 7, 11, 15]
target = 9


# [INSTRUCTIONS]
# 1. start a timer for 15 minutes and begin solving a problem
# 2. talk out loud as you're solving the problem
# 3. check for syntax errors before printing using the given example to see if your code would produce the correct answer
# 4. after the 15 minutes are done: if you found a solution record the time and space complexity. if you do not have a solution leave your code there and simply move onto the next problem
# 5. bring homework to the next class as it will be discussed at the end of the next class; solutions and/or optimal solutions will be discussed (if needed)

# PROBLEM 1 - Given a SinglyLinkedList return the product of all values in the SinglyLinkedList. Also, state complexities.
# EXAMPLE - head:1->2->3->4, answer: 24
# def singlyLinkedListProduct(head):
#     pass # replace pass with your code
# print(singlyLinkedListProduct(linkedlist))


# PROBLEM 2 - Given a TwoDimensionalArray return a List/Array/ArrayList representing the sum for each row. Also, state complexities.
# EXAMPLE - arr:[[1, 1, 1], [2, 2, 2]], answer: [3, 6]
# def twoDimensionalArraySum(arr2d):
#     pass # replace pass with your code
# print(twoDimensionalArraySum(arr2d))


# CHALLENGE PROBLEM - Given a List/ArrayList return the indices of the numbers that add up to the given target. Also, state complexities.
# EXAMPLE - arr:[2, 7, 11, 15], target=9, answer: [0, 1]
# def twoSum(arr, target):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i, j]
# print(twoSum(arr1d, target))