# Sort the Array    

num_test_case = int(input("Enter the number of test cases: "))

end_list = []
for i in range(num_test_case):
    int_array = []
    array_length = input("Enter the numer of elements in array: ")
    array = input("Enter the term you would like to check: ").split(" ")
    for elm in array:
        if (elm == ""):
            pass
        else:
            int_array.append(int(elm))
    end_list.append(sorted(int_array))

for elm in end_list:
    for inner_elm in elm:
        print(inner_elm, end=' ')
    print()