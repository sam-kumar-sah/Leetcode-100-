//961. N-Repeated Element in Size 2N Array

//output:
Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

//code:

//method-1:
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        h={}
        for i in A:
            if(i not in h):
                h[i]=1
            else:
                h[i]+=1
        
        print("h=",h)

        v=list(h.values())
        k=list(h.keys())
        return (k[v.index(max(v))])
        
ss = Solution()
print(ss.sortedSquares(A))  

//method-2:

A=[2,3,2,4,0,-1]
hashM = {}
for i in A:
    if i not in hashM:
        hashM[i] = 1
    else:
        print(i)