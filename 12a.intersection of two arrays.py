//349. Intersection of Two Arrays
'''
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''

//code:
//method-1
class Solution:
    def minSteps(self,nums1,nums2) -> int:
        n1=set(nums1)
        n2=set(nums2)
        a=(n1&n2)
        return a

nums1=[1,2,2,1]
nums2=[2,2]
ss=Solution()
print(ss.minSteps(nums1,nums2))

//method-2
class Solution:
    def minSteps(self,nums1,nums2) -> int:
        s1= set(nums1)
        s2= set(nums2)
        ans=[]
        
        for i in s1:
            if i in s2:
                ans.append(i)
                
        return(ans)