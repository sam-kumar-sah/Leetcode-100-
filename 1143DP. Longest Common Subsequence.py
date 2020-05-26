#1143. Longest Common Subsequence length
'''
Time Complexity: O(N * M) 
Space Complexity: O(N * M)
where N and M are the lengths of two input strings.
'''

//longest common subsequences string and its length.
def lcs(s1, s2):
    dp= [["" for _ in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    dp[i][j] = s1[i]
                else:
                    dp[i][j] = dp[i-1][j-1] + s1[i]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], key=len)
    cs = dp[-1][-1]
    return len(cs), cs

print(lcs("abcde", "acbde"))


//Longest Common Subsequence length
def lcs(text1,text2):
    m=len(text1)+1
    n=len(text2)+1
    dp=[[0 for _ in range(n)]for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if i==0 or j==0:
                dp[i][j]=0
            elif text1[i-1]==text2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

print(lcs("bsbininm","jmjkbkjkv"))

