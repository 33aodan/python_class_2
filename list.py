listSize = int(input("Enter the size of the list: "))

userList = []

while len(userList) < listSize:
    userInput = input("Enter an item: ")
    userList.append(userInput)

print("Your list:", userList)

listSize2 = int(input("Enter the size of the list: "))

userList2 = []

while len(userList2) < listSize2:
    userInput2 = input("Enter an item: ")
    userList2.append(userInput2)

print("Your list:", userList2)

def listmatch(x, y):
    matchingelements = []
    for i in x:
        if i in y:
            matchingelements.append(i)
        else:
            matchingelements.append("invalid lists")

    print("Matching elements:", matchingelements)

listmatch(userList,userList2)
