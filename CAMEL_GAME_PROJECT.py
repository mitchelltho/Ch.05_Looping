'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
milestraveled = 0
thirst = 0
cameltiredness = 0
nativedistance = -20
canteen = 4
done = bool(False)
print()

while done == bool(False):

    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    userchoice = input("What do you choose? ").upper()
    if userchoice == "Q":
        done = bool(True)
    elif userchoice == "A":
        print("test")
    elif userchoice == "B":
        print("test")
    elif userchoice == "C":
        milestraveled += random.randint(9,20)
        print("You have traveled " + str(milestraveled) + " Miles")
        thirst += 1
        cameltiredness += random.randint(0,3)
        nativedistance += random.randint(7,14)
    elif userchoice == "D":
        cameltiredness = 0
        print("Your camel is happy")
        nativedistance += random.randint(7,14)
    elif userchoice == "E":
        print("Miles Traveled: " + str(milestraveled))
        print("Drinks in canteen: " + str(canteen))
        print("The Natives Are " + str(abs(nativedistance)) + " Miles Behind You")
        print("Camel Tiredness " + str(cameltiredness))
    else:
        continue









