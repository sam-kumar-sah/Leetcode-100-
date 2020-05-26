//26. Remove Duplicates from Sorted Array

'''
Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the 
first two elements of nums being 1 and 2 respectively.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the 
first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
'''

//code:
def f(nums):
    if(len(nums)==0):
        return 0
    j=0
    for i in range(1,len(nums)):
        if(nums[i]!=nums[j]):
            j+=1
            print(nums[j],nums[i])
            nums[j]=nums[i]
    return j+1
nums=[1,1,2]
#nums=[0,0,1,1,1,2,2,3,3,4]
print(f(nums))