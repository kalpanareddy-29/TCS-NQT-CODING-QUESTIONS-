"""
Program: Find Second Smallest Element in a List
Description: This program finds the second smallest number in a given list without using built-in sorting.
"""

#nums=list(map(int,input().split()))
nums=[77,1,3,78,90,34,120,100]
if len(nums)>2:
    second_smallest=nums[0]
    smallest= nums[0]
    for i in nums:
        if(smallest>i):
            second_smallest=smallest
            smallest = i
        elif(second_smallest>i and i!=smallest):
            second_smallest = i
    
    print("Second smallest number in an array is ",second_smallest)
else:
    print("Second smallest number is not found")
    
