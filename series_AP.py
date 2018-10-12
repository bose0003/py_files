# Series AP

num_test_case = int(input("Enter the number of test cases: "))

end_list = []
for i in range(num_test_case):
    first_two_numbers_in_series = input("Enter the first two numbers in series: ").split(" ")
    term = int(input("Enter the term you would like to check: "))
    if (int(first_two_numbers_in_series[1]) - int(first_two_numbers_in_series[0]) == 0):
        end_list.append(int(first_two_numbers_in_series[0]))
    else:
        diff = int(first_two_numbers_in_series[1]) - int(first_two_numbers_in_series[0])
        #print(diff)
        position = (diff * term + int(first_two_numbers_in_series[0])) - diff
        end_list.append(position)

for element in end_list:
    print(element)