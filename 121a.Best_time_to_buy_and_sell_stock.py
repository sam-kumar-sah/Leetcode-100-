//121. Best Time to Buy and Sell Stock
'''
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
 design an algorithm to find the maximum profit.

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 and sell on day 5, profit = 6-1 = 5.
Not 7-1=6,as selling price needs to be larger than buying price.
'''


//code:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mprofit=0
        buy=float('Inf')
        for price in prices:
            if(price < buy):
                buy=price
                
            if(price-buy > mprofit):
                mprofit=price-buy
        return mprofit
        


prices=[7,1,5,3,6,4]
ss=solution()
print(ss.maxProfit(prices))