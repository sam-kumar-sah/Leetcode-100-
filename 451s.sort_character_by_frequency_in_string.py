//451. Sort Characters By Frequency
'''
Given a string, sort it in decreasing order based on the 
frequency of characters.

Example 1:

Input: "tree"
Output: "eert"

Example 2:

Input: "cccaaa"
Output: "cccaaa"

Example 3:

Input: "Aabb"
Output: "bbAa"
'''

//code:
class Solution(object):
    def fs(self,s):
        
        h={}
        for ch in s:
            if(ch not in h):
                h[ch]=1 
            else:
                h[ch]+=1 

        l=sorted([(h[c],c) for c in h],reverse=True)
        l1=[]
        for ch,c in l:
            l1.append(c*ch)
        
        return ''.join(l1)
        
        
s=input()
ss=Solution()
print(ss.fs(s))