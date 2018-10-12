prime_list = []
def factorial(num):
    if (num < 0):
        return "Invalid Number"
    elif (num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num -1)

for i in range(2,1000):
    if factorial(i-1) % i == (i -1):
        prime_list.append(i)

print(prime_list)