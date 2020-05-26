//231. Power of Two

'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1 (2^0=1)
Output: true 

Example 2:
Input: 16 (2^4=16)
Output: true

Example 3:
Input: 218
Output: false

'''

//code:

class solution(object):
    def sn(selfself,n):
        i=1
        while(i<n):
            i*=2
        return i==n


l = int(input())
ss = solution()
print(ss.sn(l))   #for boolean return type.
#ss.sn(l)     #for print("true/false") function