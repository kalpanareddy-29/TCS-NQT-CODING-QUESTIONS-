"""
Program: Find Most Frequent Element in a List
Description: This program counts the frequency of elements using a dictionary and prints the element with  occurrences.
"""

nums = [5,6,7,3,2,4,50,2,3,4]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency of elements:", freq)

max_key = None
max_count = 0

for k, v in freq.items():
    if v > max_count:
        max_count = v
        max_key = k

print("Value:", max_key, "it occurs", max_count, "times")
print("Most frequency element :",max_key)
