//8. String to Integer (atoi)
'''
Implement atoi which converts a string to an integer.
Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store 
integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, 
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''

//output:
'''
Example 3:
Input: "4193 with words"
Output: 4193

Example 4:
Input: "words and 987"
Output: 0

Example 5:
Input: "-91283472332"
Output: -2147483648

'''


//code:
class Solution:
    def myAtoi(self, str: str) -> int:
        num = ""
        for char in str:
            if num != "" and char in " +-":
                break
            if char in '1234567890-+':
                num += char
            elif char != " ":
                break

        if num in "+-":
            return 0
        else:
            return min(max(int(num), -2 ** 31), 2 ** 31 - 1)


if __name__ =="__main__":
    str = input()
    sr = Solution()
    print(sr.myAtoi(str))