//387. First Unique Character in a String

'''
Given a string, find the first non-repeating character in it 
and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

//code:

//method-1:
class solution(object):
    def uc(self,s):
        from collections import Counter
         
        c=Counter(s)
        for i,n in enumerate(s):
            if(c[n]==1):
                return i 
        return -1
        
s=input()
ss=solution()
print(ss.uc(s))

//method-2:

A=[2,3,2,4,0,-1]
hashM = {}
for i in A:
    if i not in hashM:
        hashM[i] = 1
    else:
        print(i)