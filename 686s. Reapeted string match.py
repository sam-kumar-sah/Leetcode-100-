//686. Repeated String Match
'''
Given two strings A and B, find the minimum number of times 
A has to be repeated such that B is a substring of it. 
If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab".
Return 3,
'''

//code:
#method-1
class Solution:
    def repeatedStringMatch(self,a,b) -> int:
        a1=len(a)
        b1=len(b)
        times = b1 // a1 + 3
        for i in range(1, times):
            print(a * i, end=" ")
            if b in a * i:
                return i
        return -1
        
#method-2
'''
import math
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        base = math.ceil(len(B) / len(A))
        for i in range(2):
            if B in A*(base + i):
                return base + i
        return -1
'''

if __name__ =="__main__":
    a = input()
    b = input()
    sr = Solution()
    print(sr.repeatedStringMatch(a,b))
