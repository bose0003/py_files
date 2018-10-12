''' Get a string and return a string that has all the words greater than 5 reversed.'''

s = input("Enter the string").split(" ")
reversed_l = []
for word in s:
    if len(word) >= 5:
        reversed_l.append(word[::-1])
    else:
        reversed_l.append(word)

print((" ").join(reversed_l))