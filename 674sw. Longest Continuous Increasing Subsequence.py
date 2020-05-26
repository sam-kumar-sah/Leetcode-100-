//674. Longest Continuous Increasing Subsequence
#Approach #1: Sliding Window

def findLengthOfLCIS(nums):       
	res=cur=0
	for i in range(len(nums)):
		if i>0 and nums[i]>nums[i-1]:
			cur+=1
		else:
			cur=1
		res=max(res,cur)
	return res
	

#Approach #2: Dynamic programming
def findLengthOfLCIS(nums):
	if not nums: return 0
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
        return max(dp)