//202. Happy Number
'''
Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

//method-1:
def sq(n):
    s = set()
    while n != 1:
        if n in s:
            return False
        s.add(n)
        print("s=",s)
        n = sum([int(i) ** 2 for i in str(n)])
        print("n=",n)
    else:
        return True

n=55
print(sq(n))


//method-2:
def isHappy(n: int):
    def sum_of_digits(n):
        sm= 0
        while n:
            sm += (n % 10) ** 2
            n //= 10
        return sm

    s = set()
    while n != 1:
        n = sum_of_digits(n)
        if n in s:
            return False
        s.add(n)
    return True