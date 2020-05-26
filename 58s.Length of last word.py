//58. Length of Last Word
'''
Given a string s consists of upper/lower-case alphabets and 
empty space characters ' ', return the length of last word 
(last word means the last appearing word if we loop from left 
to right) in the string.

If the last word does not exist, return 0.
'''

//code:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        a=s.strip()
        if(len(a)==0):
            return 0
        else:
            for i in range(len(a)):
                if(a[i]==' '):
                    l=0
                else:
                    l+=1
            return l