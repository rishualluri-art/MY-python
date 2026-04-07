x=float(input("How much money do you have."))
while True:
    e=float(input("How much money are you willing to spend."))
    b=x-e
    print("You Have",b,"remaining money.Are you willing to buy something else. type clear to exit")
    if (e<0):
        print("YOU ARE BROKE/ IN DEBT!:(")