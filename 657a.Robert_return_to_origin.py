//657. Robot Return to Origin

'''
Valid moves are R (right), L (left), U (up), and D (down). 
If the robot returns to the origin after it finishes all of 
its moves, return true. Otherwise, return false.

Example 1:
Input: "UD"
Output: true 

Example 2:
Input: "LL"
Output: false
'''

//code:
class Solution:
    def jc(self, moves: str) -> bool:
        ud=0
        lr=0
        for i in moves:
            if (i == 'U'):
                ud = ud + 1
            elif (i == 'L'):
                lr = lr + 1
            elif (i == 'R'):
                lr = lr - 1
            elif (i == 'D'):
                ud = ud - 1
        return (ud == 0 and lr == 0)

l = input()
ss = Solution()
print(ss.jc(l))   