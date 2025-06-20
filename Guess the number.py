
import random
import sys
import time

def t(x):
    time.sleep(x)


def drama_cursor(text, cursor_char='|'):
    for i in text:
        # Print character + cursor, stay on same line
        sys.stdout.write(i + cursor_char)
        sys.stdout.flush()
        t(0.025)

        # Erase the cursor (overwrite it)
        sys.stdout.write('\b')  # backspace to remove cursor
        sys.stdout.flush()
        t(0.025)

    # Optional: print final space or remove cursor
    sys.stdout.write('')  # or \n to end with newline
    sys.stdout.flush()


def position(potential,guess):
    if potential>guess:
        drama_cursor("Too High\n")
    else:
        drama_cursor("Too Low\n")


def chance(attempts,level,potential,guess):
    roll=[1,2,3,4,5,6,7,8,9,10]
    roll2=[1,2,3,4,5,0,0,0,0,0]
    roll3=[1,0,0,0,0,0,0,0,0,0]
    if level=="legendary":
        dice = roll
    elif level=="exotic":
        dice = roll2
    else :
        dice = roll3
    luck=abs(((guess-potential)/10))
    power=random.choice(dice)
    if power>luck:
        attempts[0]+=1

def common(guess,level):
    if level==1:
        attempts = [12]
    elif level==2:
        attempts = [7]
    else :
        attempts = [5]
    initial=attempts[0]
    while True:
        drama_cursor(f"You have {attempts[0]} attempts to guess the correct number.\nMake a guess: ")
        potential=int(input())
        attempts[0]-=1

        if potential!=guess:
            position(potential,guess)
        elif potential==guess:
            drama_cursor(f"The answer is {guess}. You got it correct and in only {initial-1-attempts[0]} attempts!!\n")
            break
        else:
            drama_cursor(f"You ran out of guess's .The number is {guess}. You were {abs(guess-potential)} numbers away from my guess. \n I GUESS you are not a magician.")
            drama_cursor("See what i did there:)")
            break


def legendary(guess,level):
    drama_cursor("You think you are a wizard do you now, well let us see your powers in action!! \n")
    drama_cursor("You have one attempt but there is a catch, the closer your guess is the higher the chance that i will grant you another attempt\n")
    drama_cursor("Let us see who you really are")
    attempts = [1]



    while True:
        print("\n" * 2)
        drama_cursor(f"You have {attempts[0]} attempt to guess the correct number. Good luck. \nMake a {level.upper()} guess: ")
        potential = int(input())

        attempts[0] -= 1
        attempts_2=0
        attempts_2+=1
        if potential != guess:
            chance(attempts,level,potential, guess)
            if attempts[0]==1:
                time.sleep(1)
                drama_cursor("Lucky you. You got an extra attempt. Maybe you are a wizard after all\n")
                time.sleep(1)
                position(potential, guess)
            else:
                time.sleep(2)
                drama_cursor(
                    f"You ran out of attempts's and luck .The number is {guess}.\nYou were {abs(guess - potential)} numbers away from my guess. \nI GUESS you are not as legendary as you think.\n")
                drama_cursor("See what i did there:)\n")
                break
        elif potential==guess:
            drama_cursor(f"The answer is {guess}. You got it correct and in only {attempts_2} attempts!!\n")
            print("\n" * 100)
            break
        else :
            time.sleep(2)
            drama_cursor(
                f"You ran out of attempts's and luck .The number is {guess}.\nYou were {abs(guess - potential)} numbers away from my guess. \nI GUESS you are not as legendary as you think.\n")
            drama_cursor("See what i did there:)\n")
            break

while True:
    logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
    print(logo)

    arr=["Welcome to the number Guessing Game!\n",
         "I am your host: \n",
         "The Ultralak\n",
         "Now, I am thinking of a number between 1 and 100\n",
        "Hint: a very efficient computer algorithm could be the solution instead of blindly guessing :)\n",
        "Try not to guess the same number twice\n",
         "Choose a difficulty. Type 'easy','medium', and 'hard' for skill \n'legendary','Exotic' and 'Nightmare' to flex your magic powers \nor 'exit' to well ... its in the name\n "]
    for k in arr:
        drama_cursor(k)

    number_guess = random.randint(1, 100)
    decision = input()


    chosen=False
    while not chosen:
        if decision.lower()=="easy":
            common(number_guess,1)
            chosen=True
        elif decision.lower()=="medium":
            common(number_guess,2)
            chosen=True
        elif decision.lower()=="hard":
            common(number_guess,3)
            chosen=True
        elif decision.lower()=="exit":
            drama_cursor("Thanks for playing my game")
            sys.exit()
        elif decision.lower()=="legendary":
            legendary(number_guess,"legendary")
            chosen=True
        elif decision.lower()=="exotic":
            legendary(number_guess,"exotic")
            chosen=True
        elif decision.lower()=="nightmare":
            legendary(number_guess,"nightmare")
            chosen=True
        else:
            drama_cursor("Please choose again :D \nChoose a difficulty. Type 'easy' or 'hard' or 'exit' to well ... its in the name " )
            decision = input()
    decision=input("Would you like to continue? y/n ")
    if decision=="n":
        drama_cursor("Thanks for playing my game")
        time.sleep(2)
        sys.exit()
    time.sleep(2)
    print("\n"*100)



