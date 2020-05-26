//136. Single Number
'''
Given a non-empty array of integers, every element appears 
twice except for one. Find that single one.

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

//code:
#using list comprehension
class solution(object):
    def sn(selfself,l):
        nd=[]
        for i in l:
            if(i not in nd):
                nd.append(i)
            else:
                nd.remove(i)
        return nd.pop()
'''
#using hash table
class Solution(object):
    def sN(self, l):
        ht = {}
        for i in l:
            try:
                ht.pop(i)
            except:
                ht[i] = 1
        return ht.popitem()[0]


#using math
class solution(object):
    def sn(self, nums):
        #print(set(nums))
        #print(sum(set(nums)))
        #print(sum(nums))

        return 2*sum(set(nums)) - sum(nums)
'''
l = [1, 4, 2,1,2]
ss = solution()
#sss=Solution()
print(ss.sn(l))

#print(sss.sN(l))



//using Hash Table:
def an(l):
    h={}
    for i in l:
        if(i not in h):
            h[i]=1
        else:
            h[i]+=1
    print(h)
    for i,c in enumerate(h):
        if(h[c]==1):
            return c

l=[4,1,2,1,2]
print(an(l))


