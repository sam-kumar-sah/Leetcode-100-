//123. Best Time to Buy and Sell Stock III
'''
Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 
	(price = 3),profit = 3-0 = 3. Then buy (price = 1) 
	and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), 
	profit = 5-1 = 4.
	Note that you cannot buy on day 1, buy on day 2 and sell them later, 
    You must sell before buying again.

'''



//code:

'''Time complexity  is O(n).
Algorithmic Paradigm: Dynamic Programming
'''
class solution(object):
    def tmp(self,l,n):

        p=[0]*n
        hp=l[n-1]
        lp = l[0]

        for i in range(n-2,0,-1):
            if(l[i] > hp):
                hp=l[i]
            p[i]=max(p[i+1],hp-l[i])

        for i in range(1,n):
            if(l[i] < lp):
                lp=l[i]
            p[i]=max(p[i-1],p[i]+(l[i]-lp))
        result=p[n-1]

        return result
l=[3,3,5,0,0,3,1,4]
#l=[2,30,15,10,8,25,80]
#l=[1,2,3,4,5]
n=len(l)
ss=solution()
print(ss.tmp(l,n))