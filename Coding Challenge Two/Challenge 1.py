# A password Creator
EmployeeName = input("What is your middle name: ")
EmployeeFavouritePasta = input("What is your favourite type of pasta: ")
EmployeeNumber = int(input("Give us a number between 1-100"))

while (EmployeeNumber > 100 or EmployeeNumber < 1):
    print("please enter a number between 1 - 100")
    EmployeeNumber = (input("Give us a number between 1-100"))
EmployeeNumber = str(EmployeeNumber)

EmployeeSymbol = input("Choose either & or £ symbol for your password")

EmployeePassword = (EmployeeNumber + EmployeeFavouritePasta + EmployeeName + EmployeeSymbol)
print(EmployeePassword)