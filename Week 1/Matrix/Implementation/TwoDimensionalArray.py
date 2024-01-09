twoDarray = [[1, 2], [3, 4]] # O(1) time
# O(n^2) for time if we looped but that's the same as O(r*c)

twoDarray = [[1, 2], [3, 4], [5, 6]] # O(1) time
# 3x2
# 3 x 2 = 6

# O(r*c) time
for row in range(len(twoDarray)): # O(r=3) time
    for col in range(len(twoDarray[0])): # O(c=2) time
        print(twoDarray[row][col]) # O(1) time
        print(f"twoDarray's ROW={row}, COL={col} is the number", twoDarray[row][col]) # O(1) time

twoDarray = [["Red", "Green", "Gold"],["Blue", "Black", "Silver"],["Purple", "Orange", "Yellow"]] # O(1) time
print(twoDarray[0][2]) # O(1) time
print(twoDarray[1][2]) # O(1) time
print(twoDarray[2][2]) # O(1) time
twoDarray = [["Red", "Green"],["Blue", "Black"]] # O(1) time
print(twoDarray) # O(1) time
twoDarray[0][0] = "Blue" # O(1) time
twoDarray[1][0] = "Red" # O(1) time
print(twoDarray) # O(1) time





# twoDarray = [[1, 2], [3, 4]] # O(1) time

# # Updating value in the array
# twoDarray[0][1] = 100 # O(1) time

# # Accessing cell value from given array
# print(twoDarray[1][1]) # O(1) time

# # Traverse 2D array
# for r in range(len(twoDarray)): # O(r) time
#     for c in range(len(twoDarray[0])): # O(c) time
#         print(twoDarray[r][c]) # O(1) time