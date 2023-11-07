
def findMissing_digit(mobile_number):
    digits = set("0123456789")
    mobile_digits = set(mobile_number)
    missing_digits = digits - mobile_digits

    return(missing_digits)

mobile_number = input("input mobile number here: ")

mobile_number = ''.join(filter(str.isdigit,mobile_number))

missing_digits = findMissing_digit(mobile_number)

if missing_digits:
    print("missing digits in the mobile number: ",','.join(sorted(missing_digits)))
else:
    print("no missing digits in the mobile number.")