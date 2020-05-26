//561. Array Partition I

//output:
Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and 
the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

//code:
class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])


nums = [1, 4, 3, 2]
ss = Solution()
print(ss.arrayPairSum(nums))


l=[1,4,3,2]
l.sort()
print(l)
print(l[::2])
print(sum(l[::2]))