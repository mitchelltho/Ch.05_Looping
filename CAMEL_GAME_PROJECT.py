'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
choiceBnegativeeffect = 0
milestraveled = 0
thirst = 0
cameltiredness = 0
nativetraveled = -20
canteen = 4
done = bool(True)
mysterycloak = False
userchoice = input("\033[1;33;49mWelcome To Camel Game, Press Enter To Play ").upper()
if userchoice == "":
    done = False

while done == bool(False):# Main game loop, handles whether game is over or not

    nativedistance = nativetraveled - milestraveled
    if milestraveled >= 300:
        print("\033[1;32;49mYou Win!")
        done = True
        break
    if milestraveled >= 300 and thirst == 6 or cameltiredness > 8:
        print("\033[1;35;49mYou Made It, But Died In Town")
        break
    if milestraveled >= 300 and mysterycloak == True:
        print("\033[1;38;49mAs You Walk Into Town You Receive Strange Glances From The Guards And Some Townspeople")
        print("A Mysterious Man Asks Where You Got That Cloak From")
        print("...")
        print("...")
        print("...")
        print("\033[1;32;49mYou Win?")
        done = True
        break
    if thirst == 5:
        print("\033[1;34;49mYou Are Thirsty, Either Drink From Your Canteen Or Hope You Find An Oasis")
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
            oasischance = random.randint(0,17)
            travelingmerchantchance = random.randint(0,50)
            if travelingmerchantchance == 1:
                userchoice = input("You Come Across A Mysterious Traveling Merchant, His Face Cloaked In His Hood, \n"
                                   "And His Camel Is As Dark As The Night. As You Approach Him He Asks If You \n"
                                   "Would Like To See His Wares. Do You Accept? Yes Or No? ").upper()
                if userchoice == "YES" or "Y" or "YE" or "YUP" or "YEP" or "SURE":
                    mysterymerchantkindness = random.randint(0,5)
                    if mysterymerchantkindness == 1:
                        print("The Mystery Merchant Watches You Closely As You Approach, And As You Come Close \n"
                              "He Acts Swiftly And Stabs You In The Back Before You Can Tell What's Happening And \n"
                              "You Die.")
                        done = True
                        break
                    else:
                        print("The Mystery Merchant Watches You As You Approach, And As You Come Close \n"
                        "He Pulls A Lever, Revealing A Store Of Useful Items")
                        print("A. Teleport To Either An Oasis Or Inbetween -10 And +15 Miles")
                        print("B. An Enchantment For Your Camel, Making It Never Tire Out For At least 5 Moves \n"
                              "Or Making It Slightly Slower")
                        print("C. A Mysterious Cloak With Unknown Properties")
                        print("Q. Leave")
                        userchoice = input("What Do You Choose? ").upper()
                        if userchoice == "A":
                            choiceA = random.randint(0,3)
                            if choiceA == 1:
                                canteen = 4
                                thirst = 0
                                cameltiredness = 0
                                print("\033[1;34;49mYou Teleport To An Oasis And Your Resources Are Replenished")
                            elif choiceA == 2:
                                choiceAback = random.randint(-11,-1)
                                milestraveled += choiceAback
                                print("You Were Teleported " +abs(choiceAback) + " Miles Back")
                            elif choiceA == 3:
                                choiceAforward = random.randint(0,15)
                                milestraveled += choiceAforward
                                print("You Were Teleported " +choiceAforward + " Miles Forward")
                        elif userchoice == "B":
                            choiceB = random.randint(0,3)
                            if choiceB == 1 or 2:
                                cameltiredness = -15
                                print("Your Camel Becomes Stronger")
                            if choiceB == 3:
                                choiceBnegativeeffect = random.randint(0,3)
                                print("Your Camel Is Sluggish")
                        elif userchoice == "C":
                            mysterycloak = bool(True)
                            print("You Take The Cloak And Leave")
                else:
                    print("You Pass Him Up On His Offer And He Disappears In Front Of Your Eyes In A Puff Of Smoke")
            if oasischance == 1 and travelingmerchantchance > 1:
                canteen = 4
                thirst = 0
                cameltiredness = 0
                print("\033[1;34;49mYou Stumble Across An Oasis And Your Resources Are Replenished")
                nativechance = random.randint(0,2)
                if nativechance == 1:
                    nativegain = random.randint(0,5)
                    nativetraveled += nativegain
                    print("\033[1;31;49mBut The Natives Got " + nativegain + " Closer")
            milestraveled += random.randint(5,13) - choiceBnegativeeffect
            print("You have traveled " + str(milestraveled) + " Miles")
            thirst += 1
            cameltiredness += 1
            nativetraveled += random.randint(7,15)
        elif userchoice == "C":# Ahead full speed
            oasischance = random.randint(0, 14)
            travelingmerchantchance = random.randint(0, 50)
            if travelingmerchantchance == 1:
                userchoice = input("You Come Across A Mysterious Traveling Merchant, His Face Cloaked In His Hood, \n"
                                   "And His Camel Is As Dark As The Night. As You Approach Him He Asks If You \n"
                                   "Would Like To See His Wares. Do You Accept? Yes Or No? ").upper()
                if userchoice == "YES" or "Y" or "YE" or "YUP" or "YEP" or "SURE":
                    mysterymerchantkindness = random.randint(0, 5)
                    if mysterymerchantkindness == 1:
                        print("The Mystery Merchant Watches You Closely As You Approach, And As You Come Close \n"
                              "He Acts Swiftly And Stabs You In The Back Before You Can Tell What's Happening And \n"
                              "You Die.")
                        done = True
                        break
                    else:
                        print("The Mystery Merchant Watches You As You Approach, And As You Come Close \n"
                              "He Pulls A Lever, Revealing A Store Of Useful Items")
                        print("A. Teleport To Either An Oasis Or Inbetween -10 And +15 Miles")
                        print("B. An Enchantment For Your Camel, Making It Never Tire Out For At least 5 Moves \n"
                              "Or Making It Slightly Slower")
                        print("C. A Mysterious Cloak With Unknown Properties")
                        print("Q. Leave")
                        userchoice = input("What Do You Choose? ").upper()
                        if userchoice == "A":
                            choiceA = random.randint(0, 3)
                            if choiceA == 1:
                                canteen = 4
                                thirst = 0
                                cameltiredness = 0
                                print("\033[1;34;49mYou Teleport To An Oasis And Your Resources Are Replenished")
                            elif choiceA == 2:
                                choiceAback = random.randint(-11, -1)
                                milestraveled += choiceAback
                                print("You Were Teleported " + abs(choiceAback) + " Miles Back")
                            elif choiceA == 3:
                                choiceAforward = random.randint(0, 15)
                                milestraveled += choiceAforward
                                print("You Were Teleported " + choiceAforward + " Miles Forward")
                        elif userchoice == "B":
                            choiceB = random.randint(0, 3)
                            if choiceB == 1 or 2:
                                cameltiredness = -15
                                print("Your Camel Becomes Stronger")
                            if choiceB == 3:
                                choiceBnegativeeffect = random.randint(0, 3)
                                print("Your Camel Is Sluggish")
                        elif userchoice == "C":
                            mysterycloak = bool(True)
                            print("You Take The Cloak And Leave")
                else:
                    print("You Pass Him Up On His Offer And He Disappears In Front Of Your Eyes In A Puff Of Smoke")
            if oasischance == 1 and travelingmerchantchance > 1:
                canteen = 4
                thirst = 0
                cameltiredness = 0
                print("\033[1;34;49mYou Stumble Across An Oasis And Your Resources Are Replenished")
                nativechance = random.randint(0, 2)
                if nativechance == 1:
                    nativegain = random.randint(0, 5)
                    nativetraveled += nativegain
                    print("\033[1;31;49mBut The Natives Got " + nativegain + "Closer")
            milestraveled += random.randint(10,21) - choiceBnegativeeffect
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









