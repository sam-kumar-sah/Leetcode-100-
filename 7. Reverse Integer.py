//7. Reverse Integer
'''
Input: -123
Output: -321
'''

#method-1:
def reverse(x):
        
	if x>=0:
		x=int(str(x)[::-1])
	else:
		x=-int(str(-x)[::-1])
		
	return x if x<=(2**31-1) and x>=-(2**31) else 0


//Method-2:
def reverse(self,x):
	sign=1 if x>=0 else -1
	rev=0
	x=abs(x)
	while x:
		d=x%10
		rev=rev*10+d
		x=x//10
	rev=rev*sign
	return rev if rev<=(2**31-1) and rev>=(-2**31) else 0


# solution by sam sah.
#https://www.linkedin.com/in/samsahp9/