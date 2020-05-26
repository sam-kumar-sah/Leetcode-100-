//518DP. Coin Change 2
//Total no of ways of coin change.

#1D array DP(75% faster)
class Solution(object):
    def change(self, amount, coins) :
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        print(dp)
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] = dp[j] + dp[j-coins[i]]
        print(dp)
        return dp[amount]
ss=Solution()
amount = 5
coins = [1, 2, 5]
print("c2=",ss.change(amount, coins))

#1D array DP(95% faster)
class Solution(object):
    def ch(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

#2D array DP
class Solution:
    def change(self, amount, coins):
        dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 0
        for i in range(1 , len(coins) + 1):
            for j in range(1 , amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j-coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

ss=Solution()
amount = 15
coins = [ 2,3, 5,10]
print("c2=",ss.change(amount, coins))

'''
#watch jenny lecture coin change
C\A|j= 0  1  2  3  4  5  6  7
---|------------------------------
0= | [[1, 0, 0, 0, 0, 0, 0, 0],
2= |  [1, 0, 1, 0, 1, 0, 1, 0],
3= |  [1, 0, 1, 1, 1, 1, 2, 1],
5= |  [1, 0, 1, 1, 1, 2, 2, 2],
10=|  [1, 0, 1, 1, 1, 2, 2, 2]]
'''