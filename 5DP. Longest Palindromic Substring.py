//5. Longest Palindromic Substring

#Approach 1: Dynamic Programming (Improving the Brute Force)
'''
Time Complexity: O(n2)
Space Complexity: O(n2)
'''
def lp(s):
    n=len(s)
    dp=[[False for _ in range(n)] for _ in range(n)]
    l,r=0,0

    for i in range(n):
        start,end=i,i
        while(start>=0):
            if (start==end):
                dp[start][end]=True
            elif (start+1==end):
                dp[start][end]=(s[start]==s[end])
            else:
                dp[start][end]=dp[start+1][end-1] and (s[start]==s[end])

            if(dp[start][end] and (end-start+1) > (r-l+1)):
                l=start
                r=end
            start=start-1
    return s[l:r+1]

s="babad"
print(lp(s))

#Approach 2: Expand Around Center

class Solution4:
    def longestPalindrome(self, s: str) -> str:
        #if s is '':
        #    return s
        max_len = 0
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            l = max(len1, len2)
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end+1]

    def expandFromCenter(self, s, l1, l2):
        while l1 >= 0 and l2 < len(s) and s[l1] == s[l2]:
            l1 -= 1
            l2 += 1
        return l2 - l1 - 1

s="babad"
ss=Solution4()
print(ss.longestPalindrome(s))
