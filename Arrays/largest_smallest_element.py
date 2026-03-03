"""
Program: Find Largest and Smallest Element in a List.
Description: This program finds the maximum and minimum element in a given list.
"""

#num=list(map(int,input().split()))
num=[3,4,5,8,32]
max=min=num[0]
for i in num:
    if(max<i):
        max=i
    if(min>i):
        print("hii")
        min=i
print(f"{max} is maximum and {min} is minimum")
    
