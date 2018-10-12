
# Print Tables

test_case_num = int(input("Enter the number of test cases: "))
num_list = []
for i in range(test_case_num):
    num = int(input("Enter the number for which table has to be printed: "))
    num_list.append(num)

for element in num_list:
    for i in range(1,11):
        temp = element * i
        print(temp, end = " ")
    print()

