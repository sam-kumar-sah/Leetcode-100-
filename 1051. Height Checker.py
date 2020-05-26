//1051. Height Checker

//output:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

//code:
//method-1:
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=sorted(heights)
        n=len(heights)
        c=0
        for i in range(n):
            if(h[i]!=heights[i]):
                c+=1
        return c

//method-2:
     #return sum(a != b for a, b in zip(sorted(heights), heights))
    
//method-3:
h=sorted(heights)
c=0
for i, v in enumerate(heights):
	if v != h[i]:
		c += 1
return c