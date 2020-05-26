//digital sum.py

def dsum(n):
    #print("res=",sum([int(d) for d in str(n)]))
    return sum([int(d) for d in str(n)])
def droot(n):
    result = dsum(n)
    if result < 10:
        return result
    else:
        return droot(result)

'''
if(n=="0"):
    return 0
ans=0
for i in range(0,len(n)):
    ans=(ans+int(n[i]))%9
#print(ans,end=" ")
return ans

if(ans==0):
    return 0
else:
    return ans%9
'''

n=(input())
print(droot(n))