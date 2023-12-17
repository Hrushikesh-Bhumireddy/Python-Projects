name = input("Type your anme: ")
print("Welcome",name,"to this adventure!")

answer = input("Yor are on the dirt road, it has came to an end     and you can go left or right. Which way would you like to go? (left/right) ").lower()

if answer == "left":
    a1 = input("You came to a river, would you like to walk around it or swim accross? Type walk to walk around and swim to swim accross").lower()

    if a1 == "swim":
        print("You swam accross and were eaten by an aligator. You LOSE!")
    elif a1 == "walk":
        print("You walked around many miles, ran out of staima and you lost the game!")
    else:
        print("NOt a valid option, you LOSE!")

elif answer == "right":
    a2 = input("You came to a bridge, it looks wably, do you want to cross it or head back? (cross/back) ").lower()

    if a2 == "back":
        print("You go back and you lose!")
    elif a2 == "swim":
        a3 = input("You cross the bridge and meet a stranger, would you like to talk to them?(yes/no) ").lower()

        if a3 == "yes":
            print("You talk to stranger, recieve gold, YOU WIN!")
        elif a3 == "no":
            print("You ignore them, You lose!")
        else:
            print("NOt a valid option, you LOSE!")
    else:
        print("NOt a valid option, you LOSE!")
else:
    print("NOt a valid option, you LOSE!")

print("Thanks for participating", name)