//91. Decode Ways using DP
'''
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
'''

def numDecodings(self, s: str) -> int:
	
	if not s:
		return 0
	dp=[0]*(len(s)+1)
	dp[0]=1
	for i in range(1,len(dp)):
		if s[i-1]!='0':
			dp[i]+=dp[i-1]
		if i!=1 and '10' <=s[i-2:i] <='26':
			dp[i]+=dp[i-2]
	return dp[-1]
	
	