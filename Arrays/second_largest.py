"""
Program: Find Second Largest Element in a List
Description: This program finds the second largest number in a given list without using built-in sorting.
"""

#nums=list(map(int,input().split()))
nums=[2,2,1,3,78,90,34,120,100]
if len(nums)>2:
    second_largest=nums[0]
    largest= nums[0]
    for i in nums:
        if(largest<i):
            second_largest=largest
            largest = i
        elif(second_largest<i and i!=largest):
            second_largest = i
    
    print("Second Largest number in an array is ",second_largest)
else:
    print("Second largest number is not found")



Here we can also use sorting method and use -2 index to get second largest  
"""
nums = list(set(nums))  # remove duplicates
nums.sort()
if len(nums) > 1:
    print("Second Largest number is:", nums[-2])
else:
    print("Second largest not found")"""
