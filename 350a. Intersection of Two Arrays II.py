//350. Intersection of Two Arrays II

//output:
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

//code:
//method-1:

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
nums1.sort()
nums2.sort()
a,b=0,0
l1,l2=len(nums1),len(nums2)
l=[]
while(l1>a and l2>b):
    if(nums1[a]==nums2[b]):
        l.append(nums1[a])
        a+=1
        b+=1
    elif(nums1[a] < nums2[b]):
        a+=1
    else:
        b+=1
print(l)

//method-2
'''using Has method'''

from collections import Counter
n1 = [4,9,5]
n2 = [9,4,9,8,4]
h={}
l=[]
for i in n1:
    if(i not in h):
        h[i]=1
    else:
        h[i]+=1
for i in n2:
    if(i in h):
        h[i]-=1
        if(h[i]==0):
            del h[i]
        l.append(i)
print(l)
