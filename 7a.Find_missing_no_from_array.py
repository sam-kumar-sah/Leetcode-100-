//268. Missing Number

'''
Given array contains n distinct nums taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

Example 1:
Input: [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
'''

//code:
#general method
class Solution:
    def jc(self,l):
        s1,s2=0,0
        s1=sum(l)
        for i in range(len(l)):
            s2+=i
        return abs(s2-s1)

#using hashset
class solution(object):
    def sam(self,l):
        hashset=set(l)
        n=len(l)+1
        for i in range(n):
            if(i not in hashset):
                print(i)
                return i

l = [3,0,1]
ss = solution()
print(ss.sam(l))  