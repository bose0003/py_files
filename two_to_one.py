'''
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2. 
#Examples: 
# ``` 
# a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
# a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz" ```
'''

def longest(s1,s2):
    s3 = s1 + s2
    l = []
    for i in s3:
        if i not in l:
            l.append(i)
    l = sorted(l)
    return "".join(str(i) for i in l)

    # return "".join(sorted(set(a1 + a2)))

print(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))