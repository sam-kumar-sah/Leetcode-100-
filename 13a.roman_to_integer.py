//13. Roman to Integer
'''
Roman numerals are represented by seven different symbols: 
I, V, X, L, C, D and M.

Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

//CODE:
class solution(object):
    def ri(self,s):
        roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        t=0
        for i in range(len(s)-1):
            a=s[i]
            b=s[i+1]
            if(roman[a] < roman[b]):
                t-=roman[a]
            else:
                t+=roman[a]
        t+=roman[s[-1]]
        return t

s=input()
ss=solution()
print(ss.rri(s))

