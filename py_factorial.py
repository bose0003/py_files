# Program for factorial of a number
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. 
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.
# Factorial can be calculated using following recursive formula.

#   n! = n * (n-1)!
#   n! = 1 if n = 0 or n = 1 


def factorial(num):
    if (num < 0):
        return "Invalid Number"
    elif (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num -1)

num = int(input("Enter the number to check: "))

print(factorial(num))
