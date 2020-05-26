//1347. Minimum Number of Steps to Make Two Strings Anagram
'''
Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
'''

//code:
from collections import defaultdict
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count=defaultdict(int)

        for i in s:
            count[i]+=1
        print(count)

        for i in t:
            count[i]-=1
        print(count)
        res=0
        for i in count.values():
            if i > 0:
                res += i
        return res
        #return sum(abs(i) for i in alphabet.values())//2


s=input()
t=input()
ss=Solution()
print(ss.minSteps(s,t))