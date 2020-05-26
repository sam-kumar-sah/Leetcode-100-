//791. Custom Sort String

//output:
Example 1:
Input:  S = "cba"
		T = "abcd"
Output: "cbad"

Example-2:
S = "cbafg"
T = "abcd"
o/p: cbad

//code:
from  collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        a=''
        count=Counter(T)
        for i in S:
            a+=i*count[i]
            count[i]=0
        for i in count:
            a+=i*count[i]
            
        return a
        
S=input()
T=input()
ss=Solution()
print(ss.customSortString(S,T))
