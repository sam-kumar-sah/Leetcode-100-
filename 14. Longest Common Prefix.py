//14. Longest Common Prefix

'''
Input: ["flower","flow","flight"]
Output: "fl"
'''
#Method-1 (using enumerate)
class Solution:
    def LCP(self, strs: List[str]) -> str:
                
        if not strs:
            return ""
        s=min(strs,key=len)
        for i,char in enumerate(s):
            for w in strs:
                if w[i]!=char:
                    return s[:i]
        return s

#Method-2 (using enumerate(zip(*strs)))
def LCP(strs):
    if not strs:
        return ""
    for i,char in enumerate(zip(*strs)):
        
        # ["flower","flow","flight"]
        # print(i,char,set(char))
        # 0 ('f', 'f', 'f') {'f'}

        if len(set(char))>1:
            return strs[0][:i]
    else:
        return min(strs)
 
#Method-3 (using min,max)
def longestCommonPrefix(self, strs):
    if not strs:
        return ""
    min_s = min(strs)
    max_s = max(strs)
    if not min_s:
        return ""
    for i in range(len(min_s)):
        if max_s[i] != min_s[i]:
            return max_s[:i]
    return min_s[:]


    
ss=solution()
strs=["dog","racecar","car"]
print("LCP=",LCP(strs))


		
		