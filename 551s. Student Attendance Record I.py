//551. Student Attendance Record I

'''
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
'''

//code:
import re
def sq(s):
    
    #return not re.search('A.*A|LLL', s)
    #return not (s.count('A') > 1 or 'LLL' in s)
    
    if(s.count('A')<=1):
        if('LLL' not in s):
            return True
        else:
            return False
    else:
        return False

s=input()
print(sq(s))