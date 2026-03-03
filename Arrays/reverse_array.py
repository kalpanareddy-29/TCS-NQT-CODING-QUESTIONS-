"""
Program: Reverse an Array (In-Place Method)
Description: This program reverses an array without using extra space by swapping elements from both ends.
"""

arr = [2, 3, 55, 11, 22, 8]

n = len(arr)

for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
  
print("Reversed array:", arr) # this is without using extra space


#Here we use extra space 
arr = [2, 3, 55, 11, 22, 8]
reversed_arr = []
n = len(arr)

for i in range(n - 1, -1, -1):
    reversed_arr.append(arr[i])

print("Original array:", arr)
print("Reversed array:", reversed_arr)
