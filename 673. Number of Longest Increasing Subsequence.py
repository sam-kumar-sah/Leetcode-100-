//673. Number of Longest Increasing Subsequence

'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are 
[1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence 
is 1, and there are 5 subsequences' length is 1, so output 5.
'''
class Solution:
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1 for i in range(n)]
        cnt = [1 for i in range(n)]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        cnt[j] = cnt[i]
                    elif dp[i] + 1 == dp[j]:
                        cnt[j] += cnt[i]
        curmax = max(dp)
        res = 0

        for i, v in enumerate(dp):
            if v == curmax:
                res += cnt[i]
        return res
#a=[1,3,5,4,7]
a=[2,2,2,2]
ss=Solution()
print(ss.findNumberOfLIS(a))