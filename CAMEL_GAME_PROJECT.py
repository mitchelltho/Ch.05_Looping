'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
milestraveled = 0
thirst = 0
cameltiredness = 0
nativetraveled = -20
canteen = 4
done = bool(True)
userchoice = input("\033[1;33;49mWelcome To Camel Game, Press Enter To Play ").upper()
if userchoice == "":
    done = False

while done == bool(False):# Main game loop, handles whether game is over or not

    nativedistance = nativetraveled - milestraveled
    if milestraveled >= 300:
        print("\033[1;32;49mYou Win!")
        done = True
    if milestraveled >= 300 and thirst == 6 or cameltiredness > 8:
        print("\033[1;35;49mYou Made It, But Died In Town")
    if thirst == 5:
        print("\033[1;34;49mYou Are Thirsty")
    elif thirst == 6:
        print("\033[1;31;49mYou Have Died Of Thirst!")
        done = True
    if cameltiredness > 5:
        print("\033[1;33;49mYour Camel Is Tired")
    elif cameltiredness > 8 and done == False:
        print("\033[1;31;49mYour Camel Is Dead!")
        done = True
    if nativedistance >= 0:
        print("\033[1;31;49mThe Natives Caught You!")
        done = True
    elif nativedistance >= 10:
        print("\033[1;38;49mThe Natives Are Getting Close")
    if done == False:
        print("\033[1;38;49mA. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
    if done == False:
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
            oasischance = random.randint(0,16)
            if oasischance == 1:
                canteen = 4
                thirst = 0
                cameltiredness = 0
                print("\033[1;34;40mYou Stumble Across An Oasis And Your Resources Are Replenished")
                nativechance = random.randint(0,2)
                if nativechance == 1:
                    nativegain = random.randint(0,5)
                    nativetraveled += nativegain
                    print("\033[1;31;40mBut The Natives Got " + nativegain + "Closer")
            milestraveled += random.randint(5,13)
            print("You have traveled " + str(milestraveled) + " Miles")
            thirst += 1
            cameltiredness += 1
            nativetraveled += random.randint(7,15)
        elif userchoice == "C":# Ahead full speed
            oasischance = random.randint(0, 13)
            if oasischance == 1:
                canteen = 4
                thirst = 0
                cameltiredness = 0
                print("\033[1;34;40mYou Stumble Across An Oasis And Your Resources Are Replenished")
                nativechance = random.randint(0, 2)
                if nativechance == 1:
                    nativegain = random.randint(0, 5)
                    nativetraveled += nativegain
                    print("\033[1;31;40mBut The Natives Got " + nativegain + "Closer")
            milestraveled += random.randint(10,21)
            print("You have traveled " + str(milestraveled) + " Miles")
            thirst += 1
            cameltiredness += random.randint(1,4)
            nativetraveled += random.randint(7,15)
        elif userchoice == "D":# Stop for the night
            cameltiredness = 0
            print("Your camel is happy")
            nativetraveled += random.randint(7,15)
        elif userchoice == "E":# Status Check
            print("Miles Traveled: " + str(milestraveled))
            print("Drinks in canteen: " + str(canteen))
            print("The Natives Are " + str(abs(nativedistance)) + " Miles Behind You")
            print("Camel Tiredness " + str(cameltiredness))
        else:
            continue









