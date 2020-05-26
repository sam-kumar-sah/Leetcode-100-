//287. Find the Duplicate Number

'''
Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
'''

//code:
//method-1:
def findDuplicate(nums):
        a=0
        for i in nums:
            if(nums.count(i)>1):
                a=i
                break
        return a
		
//method-2:
def findDuplicate(nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

//method-3:
def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)	
				