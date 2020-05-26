//70. Climbing Stairs

'''
You are climbing a stair case.It takes n steps to reach to top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Example 3:
Input: 9
Output: 55

'''


//code:
#using Fibonacci series using recursion
//Time Complexity: O(2^n) or exponential.

class solution(object):
    def fib(self,n):
        if(n<=2):
            return n
        else:
            a=self.fib(n-1)+self.fib(n-2)
            return a

#using dynamic programming
//Time Complexity: O(n), Space Complexity : O(n)

class solution(object):
    def dpp(self,n):
        dp=[ 0 for x in range(n+1)]
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]

n=int(input())
ss = solution()
#print(ss.dpp(n))   
print(ss.fib(n))