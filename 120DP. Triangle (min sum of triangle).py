#120. Triangle (min sum of triangle) 
#using Dynamic programming
'''
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''
def mst(triange):
    if not triangle:
        return 0
    m=len(triangle)
    dp=triangle[-1]
    for i in range(m-2,-1,-1):
        for j in range(i+1):
            print(triangle[i][j],dp[j],dp[j+1])
            dp[j]=min(dp[j],dp[j+1])+triangle[i][j]
        print(dp)
    return dp[0]

triangle=([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ])
print("mst=",mst(triangle))

