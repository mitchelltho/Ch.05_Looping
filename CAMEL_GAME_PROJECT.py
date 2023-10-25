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

while done == bool(False):# Main game loop, handles whether game is over or not


    if milestraveled >= 300:
        print("You Win!")
        done = True
    if thirst == 5:
        print("You Are Thirsty")
    elif thirst == 6:
        print("You Have Died Of Thirst!")
        done = True
    if cameltiredness > 5:
        print("Your Camel Is Tired")
    elif cameltiredness > 8 and done == True:
        print("Your Camel Is Dead!")
        done = True
    if nativedistance >= 0:
        print("The Natives Caught You!")
        done = True
    elif nativedistance >= 10:
        print("The Natives Are Getting Close")
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    userchoice = input("What do you choose? ").upper()
    if userchoice == "Q":# Quit
        done = bool(True)
    elif userchoice == "A":# Drink from your canteen
        if canteen > 0:
            canteen -= 1
            thirst = 0
        else:
            print("You have no water")
    elif userchoice == "B":# Ahead moderate speed
        milestraveled += random.randint(5,13)
        print("You have traveled " + str(milestraveled) + " Miles")
        thirst += 1
        cameltiredness += 1
        nativedistance += random.randint(7,15)
    elif userchoice == "C":# Ahead full speed
        milestraveled += random.randint(10,21)
        print("You have traveled " + str(milestraveled) + " Miles")
        thirst += 1
        cameltiredness += random.randint(1,4)
        nativedistance += random.randint(7,15)
    elif userchoice == "D":# Stop for the night
        cameltiredness = 0
        print("Your camel is happy")
        nativedistance += random.randint(7,15)
    elif userchoice == "E":# Status Check
        print("Miles Traveled: " + str(milestraveled))
        print("Drinks in canteen: " + str(canteen))
        print("The Natives Are " + str(abs(nativedistance)) + " Miles Behind You")
        print("Camel Tiredness " + str(cameltiredness))
    else:
        continue









