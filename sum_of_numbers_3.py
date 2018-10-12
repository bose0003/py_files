'''
Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
'''

def get_sum(a, b):
    sum = 0
    if a == b:
        return a
    elif a > b:
        for i in range(b, a+1):
            sum += i
    else:
        for i in range(a, b + 1):
            sum += i

    return sum

    # return sum(xrange(min(a,b), max(a,b)+1))

    
print(get_sum(1, 0)) #== 1   // 1 + 0 = 1
print(get_sum(1, 2)) # == 3   // 1 + 2 = 3
print(get_sum(0, 1)) # == 1   // 0 + 1 = 1
print(get_sum(1, 1)) # == 1   // 1 Since both are same
print(get_sum(-1, 0)) # == -1 // -1 + 0 = -1
print(get_sum(-1, 2)) # == 2  // -1 + 0 + 1 + 2 = 2