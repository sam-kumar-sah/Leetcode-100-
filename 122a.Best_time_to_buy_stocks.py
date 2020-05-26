'''122. Best Time to Buy and Sell Stock II'''
'''
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 and sell on day 3,profit=5-1=4.
    Then buy on day 4 and sell on day 5,profit = 6-3 = 3.
'''

//code:
class solution(object):
    def maxProfit(self,prices):
        ans=0
        for i in range(1,len(prices)):
            if(prices[i]-prices[i-1]>0):
                ans+=prices[i]-prices[i-1]
                print(ans)
        return ans

prices=[1,2,3,4,5]
ss=solution()
print(ss.maxProfit(prices))
print()

