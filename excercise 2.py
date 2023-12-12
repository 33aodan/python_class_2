def show_employee(name,salary=9000):
    statement = f"Name: {name} Salary: {salary}"
    return statement

x = show_employee("Ben", 12000)
y = show_employee("Jessa")
print(x)
print(y)
