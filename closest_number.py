
# test_cases = int(input("Enter the number of test cases: "))

# end_result_list = []
# for _ in range(test_cases):
#     inputs = input("Enter the 2 numbers to test: ").split(" ")
#     diff = abs(int(inputs[0])) - abs(int(inputs[1]))
#     quotient = (abs(diff) // abs(int(inputs[1]))) + 1
#     if (quotient == 0):
#         if (int(inputs[0]) < 0):
#             end_result_list.append(- (int(inputs[1])))
#         else:
#             end_result_list.append(int(inputs[1]))
#     else:
#         if (int(inputs[0]) < 0):
#             end_result_list.append(-(int(inputs[1]) * quotient))
#         else:
#             end_result_list.append((int(inputs[1]) * quotient))

# for elm in end_result_list:
#     print(elm)

# test_cases = int(input())

# end_result_list = []
# for _ in range(test_cases):
#     inputs = input().split(" ")
    
#     n = int(inputs[0])
#     m = int(inputs[1])

#     quotient = n // m

#     closest_first = m * quotient

#     if n*m > 0:     # Positivity Check
#         closest_second = m * (quotient + 1)
#     else:
#         closest_second = m * (quotient - 1)

#     if (abs(n - closest_first) < abs(n - closest_second)):
#         end_result_list.append(closest_first)
#     else:
#         end_result_list.append(closest_second)


# for elm in end_result_list:
#     print(elm)
import math
final_list = []

test_case = int(input("Enter the number of test cases: "))
for _ in range(test_case):
    inputs = input().split(" ")

    if abs(int(inputs[0])) > abs(int(inputs[1])):
        m = int(inputs[0])
        n = int(inputs[1])
    else:
        m = int(inputs[1])
        n = int(inputs[0])

    if abs(m) - abs(n) > abs (n):
        if m > 0:
            quo = m // n
            closest_num = quo * n
            closest_num_one = (quo + 1) * n
            if abs(m - closest_num) > abs(m - closest_num_one):
                final_list.append(closest_num_one)
            else:
                final_list.append(closest_num)
        if m < 0:
            quo = abs(m) // n
            closest_num_one = (quo + 1) * n
            final_list.append(-(closest_num_one))
    else:
        if m < 0 or n < 0:
            final_list.append(-(abs(n)))
        else:
            final_list.append(abs(m))
for elm in final_list:
    print(elm)