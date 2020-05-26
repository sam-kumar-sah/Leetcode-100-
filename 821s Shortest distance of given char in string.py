//821. Shortest Distance to a Character
'''
Find the shortest distance in a string from a given character.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

example 2:
aabecbgeeasde
[3, 2, 1, 0, 1, 2, 1, 0, 0, 1, 2, 1, 0]

'''

//code:
class solution(object):
    def merge(self,s,ch):
        index_nums = []
        for i, letter in enumerate(s):
            if letter == ch:
                index_nums.append(i)
        ans = []
        for j, word in enumerate(s):
            distance = [abs(j - num) for num in index_nums]
            ans.append(min(distance))
        return ans


s=input()
ss=solution()
print(ss.merge(s,'e'))