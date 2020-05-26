//1. Two Sum
'''
Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

//code:
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(target-nums[i]==nums[j]):
                    return(i,j)

nums = [2, 7, 11, 15]
target = 9
ss=Solution()
print(ss.twoSum(nums,target))