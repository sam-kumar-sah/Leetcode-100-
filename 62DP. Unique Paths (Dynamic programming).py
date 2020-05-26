#62. Unique Paths (Dynamic programming)
'''
Time complexity is O (m * n)
Space complexity is O (m * n)
'''
class solution(object):
//Method-1
    def uniquepaths(self,m,n):

        dp=[[0]*n for i in range(m)]
        for i in range(m):
            dp[i][0]=1
        for i in range(n):
            dp[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]

//Method-2
    def uniquepaths(self,m,n):
        dp=[[1]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    continue
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[m-1][n-1]



m,n=7,3
a,b=3,3
print("sam=",ss.uniquepaths(m,n))
print("sam=",ss.uniquepaths(a,b))

'''
[[1, 1, 1],
 [1, 0, 0],
 [1, 0, 0]]

[[1, 1, 1],
 [1, 2, 3],
 [1, 3, 6]]
'''