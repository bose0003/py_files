
# Add two fractions

def addFraction(num1, den1, num2, den2):
    #Code here
    if (den1 == den2):
        new_num = num1+num2
        new_den = den1
        divide_by = gcd(new_num, new_den)
        new_num = new_num // divide_by
        new_den = new_den // divide_by
        #print(new_num, new_den)
    else:
        new_den = den1 * den2
        new_num = num1 * den2 + num2 * den1
        divide_by = gcd(new_num, new_den)
        new_num = new_num // divide_by
        new_den = new_den // divide_by
    print(str(new_num) + "/" + str(new_den))
        
def gcd(num1, num2):
    if (num2 > num1):
       num1, num2 = num2, num1
    
    if (num1 < 0 or num2 < 0):
        return "Invalid"
    else:
        if num1 == 0:
            return num2
        elif num2 == 0:
            return num1
        else:
            r = num1 % num2
            return gcd(num2, r)

fractions = (input("Enter the 2 fractions as 4 elements with space: ")).split(" ")
num1 = int(fractions[0])
den1 = int(fractions[1])
num2 = int(fractions[2])
den2 = int(fractions[3])

addFraction(num1, den1, num2, den2)