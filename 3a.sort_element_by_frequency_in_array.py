//Sort list elements by frequency


//code:
class solution(object):
    def sf(self,l):
        
        from collections import Counter
        l1=sorted(l)
        a=sorted(l1,key=l1.count,reverse=True)
        return str(a) 
        
l=[1,4,3,7,5,5,2,1,1,7]
ss=solution()
print(ss.sf(l))

//output:
[1, 1, 1, 5, 5, 7, 7, 2, 3, 4]
