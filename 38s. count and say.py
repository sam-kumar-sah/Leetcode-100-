#38. count and say
'''
1.     1
2.     11
3.     21
4.     1211
5.     111221
'''
Input: 4
Output: "1211"

def countAndSay(n):
    res = '1'
    for i in range(n-1):
        new_res, pre_char, count = '', res[0], 0
        for j in range(len(res)):
            if res[j] == pre_char:
                count += 1
            else:
                new_res += str(count) + pre_char
                count = 1
                pre_char = res[j]
        res = new_res + str(count) + pre_char
    return res

n=4
print(countAndSay(n))
