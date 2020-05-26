//There are two sorted arrays nums1 and nums2 of size m 
    and n respectively.
'''
Find the median of the two sorted arrays. The overall run 
time complexity should be O(log (m+n)).

'''
//code:

class solution(object):
    def merge(self,l1,l2):
        l=l1+l2
        l.sort()
        print("l=",l)
        a=len(l)
        r=0
        if(a%2!=0):
            r=l[(a)//2]

            return r
        else:
            r=(l[(a-1)//2]+l[(a)//2])/2
            return r

l1= [1, 2]
l2 = [3,4]

s=solution()
print(s.merge(l1,l2))

//output:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5