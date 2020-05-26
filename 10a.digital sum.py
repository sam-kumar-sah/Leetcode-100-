//258. Add Digits

//output:
'''
Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
'''


//method-1:
class Solution:
    def addDigits(self, num: int) -> int:
        n=num
        s=0
        while(n>0):
            s+=(n%10)
            n//=10
            if(n==0 and s>=10):
                n=s
                s=0
        return s


num=int(input())
ss=Solution()
print(ss.addDigits(num))



//method=2
def addDigits(self, num: int) -> int:
        if num<10:
            return num
        num = (num-1)%9
        print(num+1)
        return num+1
		
//method-3:
def addDigits(self, num: int) -> int:
        if not num: 
			return 0
        return 1 + (num - 1) % 9
    
//method-4:
def addDigits(self, num: int) -> int:
        if (num<10):
            return num
        else:
            if num%9:
                return num%9
            else:
                return 9
        
//method-5:
def addDigits(self, n: int) -> int:
        idx = 0
        res = 0

        while (idx <= len(str(n))):
            digit = n // 10**idx % 10
            res += digit
            idx += 1

        if len(str(n)) == 1:
            return n
        else:
            return self.addDigits(res)