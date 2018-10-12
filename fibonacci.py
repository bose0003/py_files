#!/bin/python3

import sys

def cal_sum(up_limit):
    a = 0
    b = 1
    show = 0
    total = 0    
    
    while (show <= up_limit):
        show = a + b
        a = b
        b = show
        #print(show)
        if show <= up_limit:
            if (show % 2 == 0):
                total = total + show
                #print(show, total)
    
    return total

lst = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total = cal_sum(n)
    lst.append(total)

for _ in lst:
    print(_)
