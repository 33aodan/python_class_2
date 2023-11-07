userNum = int(input("pick a number "))
def factorial(num):
    result = 1

    for i in range(1, num+1):
        result *=i

    return result
result = factorial(userNum)
print(f"the factorial of {userNum} is {result}")

