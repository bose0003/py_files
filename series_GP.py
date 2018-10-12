
# Geometric Progression

# To find the GP, we need to find the common ration, ie; ratio of 2nd and 1st element
# Then to find the nth position we multiply first number in sequence to the common_ratio with power of n-1

import math

num_test_case = int(input("Enter the number of test cases: "))

end_list = []
for i in range(num_test_case):
    first_two_numbers_in_series = input("Enter the first two numbers in series: ").split(" ")
    n = int(input("Enter the term you would like to check: "))

    common_ratio = int(first_two_numbers_in_series[1]) / int(first_two_numbers_in_series[0])

    gp = math.floor((int(first_two_numbers_in_series[0])) * (common_ratio ** (n-1)))
    end_list.append(gp)

for elm in end_list:
    print(elm)