#64. minimun path sum

def mps(grid):
    if not grid or not grid[0]:
        return 0
    m,n=len(grid),len(grid[0])
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                ans=0
            elif i==0:
                ans=grid[i][j-1]
            elif j==0:
                ans=grid[i-1][j]
            else:
                ans=min(grid[i][j-1],grid[i-1][j])
            grid[i][j]=ans+grid[i][j]
    return grid[m-1][n-1]
grid=[
  [1,3,11],
  [0,5,1],
  [4,4,1]
]
print("ans=",mps(grid))