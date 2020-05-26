//53. Maximum Subarray

'''
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

//code:
//method-1:
def ms(nums):
    em=nums[0]
    im=nums[0]
    for i in nums[1:]:
        if(i < em+i):
            em+=i
        else:
            em=i
        if(im < em):
            im=em
    return im

nums=[-2,-1]
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(ms(nums))

//method-2:
def mss(nums):
    if not nums:
        return 0
    n=len(nums)
    cur=prev=0
    res=float("-Inf")
    for i in range(n):
        cur=nums[i]+(prev if prev >0 else 0)
        prev=cur
        res=max(res,cur)
    return res

nums=[-2,-1]
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(mss(nums))