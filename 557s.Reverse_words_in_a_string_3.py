//557. Reverse Words in a String III

'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
'''

//code:

class Solution:
    def reverseWords(self, s: str) -> str:
        s=(s.split())
        ss=[]
        for i in s:
            ss.append(i[::-1])
            
        return ' '.join(ss)
		
        
s="Let's take LeetCode contest"     
ss=Solution()
print(ss.reverseWords(s))