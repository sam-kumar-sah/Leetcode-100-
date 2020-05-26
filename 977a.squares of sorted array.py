//977. Squares of a Sorted Array

//output:
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

//code:
class Solution:
    def sortedSquares(self, A):
        l = []
        for i in A:
            l.append(i ** 2)
        l.sort()
        return l


A = [-4, -1, 0, 3, 10]
ss = Solution()
print(ss.sortedSquares(A))