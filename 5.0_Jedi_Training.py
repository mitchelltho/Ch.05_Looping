# 5.0 Jedi Training (50pts)  Name:________________

'''
 1. Make the following program work. LIST THE 3 MISTAKES (5pts)
'''
'''
print("This program takes three integers and returns the sum.")
total = 0
for i in range(3):
    x = int(input("Enter a number: "))
    total += x
print("The total is: " + str(total))
'''
#1 added + in the print before the total, replacing the ,
#2 replaced i with x in the total += x line
#3 added spaces in the total += i line
#4 replaced the x in the final print line with total
#5 added int before the input
#6 added str before printing the total


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive. (5pts)
'''
'''
x = 0
for i in range(50):
    i += 1
    x += 2
    print(x)
'''



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop. (5pts)
'''
'''
x = 10
while x >= 0:
    print(x)
    x -= 1
print("Blast off!")
'''



'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive). (5pts)
'''
import random
# leaving import random out of comment just in case
'''
x = random.randint(1, 10)
print(x)
'''




'''
  5. 7 NUMBER ANALYSIS (5pts)
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
'''
positive = 0
negative = 0
zero = 0
total = 0
for i in range(7):
    i += 1
    x = int(input("Give me a number: "))
    total += x
    if x >= 1:
        positive += 1
    elif x <= -1:
        negative += 1
    else:
        zero += 1
print("Your total is: " + str(total) + "\nNumber of positives: " + str(positive) + "\nNumber of negatives: "
      + str(negative) + "\nNumber of zeros: " + str(zero))
'''




'''
6. COIN TOSS PROGRAM (10pts)
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
'''
heads = 0
tails = 0
for i in range(50):
    i += 1
    coin = random.randint(0, 1)
    if coin == 0:
        heads += 1
        print("Heads!")
    else:
        tails += 1
        print("Tails!")
print("Number of heads: " + str(heads) + "\nNumber of tails: " + str(tails))
'''


'''
ROSHAMBO PROGRAM (15pts)
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round, tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits, print an end game message and their win/loss/tie record

'''
wins = 0
losses = 0
draws = 0
playing = 1
print("\033[1;38;49m Enter 4 at any draw to quit the program")
while playing == 1:
    draw = random.randint(1, 3)
    playerdraw = int(input("\033[1;38;49m Pick your draw!\nRock = 1\nPaper = 2\n Scissors = 3\n"))
    if playerdraw == 4:
        playing -= 1
    elif playerdraw == (draw - 2) or playerdraw == (draw + 1):
        wins += 1
        print("\033[1;32;49m You Win!")
    elif playerdraw == (draw - 1) or playerdraw == (draw + 2):
        losses += 1
        print("\033[1;31;49m You Lose!")
    else:
        draws += 1
        print("\033[1;38;49m Draw!")
    if playerdraw == 1:
        print("\033[1;38;49m You drew Rock")
    elif playerdraw == 2:
        print("You drew Paper")
    elif playerdraw == 3:
        print("You drew Scissors")
    if draw == 1:
        print("\033[1;38;49m They drew Rock")
    elif draw == 2:
        print("They drew Paper")
    elif draw == 3:
        print("They drew Scissors")

print("\033[1;32;49m Your wins: " + str(wins))
print("\033[1;31;49m Your losses: " + str(losses))
print("\033[1;38;49m Your draws: " + str(draws))
print("\033[1;32;49m Thanks for playing!")



