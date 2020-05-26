//27. Remove Element

'''
Given an array nums and a value val, remove all instances 
of that value in-place and return the new length.

Do not allocate extra space for another array,

Example 1:
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, 
with the first five elements of nums containing 0,1,3,0,4.
'''

//code:
class solution(object):
    def rv(self,l,v):
        c=0
        l1=[]
        #1st way doesn't work on leetcode
        for i in l:
            if(i!=v):
                c=c+1
                l1.append(i)
        #2nd way works
        while(l.count(v)):
            l.remove(v)
        print("l=",l," len=",len(l))
        print("l1=",l1, " len=",c)
        return len(l)

l = [0,1,2,2,3,0,4,1,2]
v=2
ss = solution()
print(ss.rv(l,v))  