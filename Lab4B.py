# Welcome!
# Please input a number: 100
# What would you like to do with this number:
# 0) Get the additive inverse of the number
# 1) Get the reciprocal of the number
# 2) Square the number
# 3) Cube the number
# 4) Exit the program
# 0
# The additive inverse of 100.0 is -100.0


print(f"Welcome!")
nomber = float(input(f"Please input a number: "))
decision = int(input(f"What would you like to do with this number:\n0) Get the additive inverse of the number \n1) Get the reciprocal of the number \n2) Square the number \n3) Cube the number \n4) Exit the program\n"))

match decision:
    case 0:
        nomber0 = nomber * (-1)
        print(f"The additive of {nomber} is {nomber0:0.2f}")
    case 1:
        if nomber == 0:
            print("Cannot divide by 0!")
        else:
            nomber1 = nomber**-1
            print(f"The reciprocal of {nomber} is {nomber1:0.3f}")
    case 2:
        nomber2 = nomber**2
        print(f"the square of {nomber} is {nomber2:0.1f}")
    case 3:
        nomber3 = nomber**3
        print(f"The cube of {nomber} is {nomber3:0.1f}")
    case 4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid option!")
