'''
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

Note:
this kata was recently attributed to @mclean, which is false (see his comment). Gosts at Codewars or bad joke? // g964
'''

def accum(s):
    l = []
    for i in range(1, len(s)+ 1):
        l.append("".join(i * s[i-1]).capitalize())
    return "-".join(str(i) for i in l)

print(accum("abcd"))
print(accum("RqaEzty")) # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))   