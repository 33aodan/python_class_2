user = int(input("how long do you want your fibonacci statement to be? "))
n1, n2 = 0, 1
count = 0

if user <= 0:
    print("number must be positive")
elif user == 1:
    print(f"fibonacci series is up to {user}: ", n1)
else:
    print("fibonacci series:")
    while count <= user:
        print(n1)
        n3 = n1+n2
        n1=n2
        n2=n3
        count += 1