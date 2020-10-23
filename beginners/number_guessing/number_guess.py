import random

def guess_the_number():
    x = random.randint(1, 100)
    points = 5

    while points > 0:
        guess = int(input("Guess a number: "))
        
        if guess == x:
            print("Wow you guess right! " + points + " points to Gryffindor.")
            break
        else:
            points -= 1
            if points % 2 == 0:
                if guess > x:
                    print("Your guess was too big.")
                else:
                    print("Think smaller")
            elif points == 3:
                if x % 10 == 0:
                    print("Try an even number.")
                else:
                    print("It's an odd number.")
            elif points == 1:
                print("You got 1 try left buddy.")
                if x % 10 == 0:
                    print("It's a multiple of 10")
                else:
                    print("There's no 0 in the ones place.")
    if points == 0:
        print("YOU LOSE!!! The correct answer was " + str(x) + ".")

print("NUMBER GUESSING GAME")
print("A random number between 1 and 100 will be picked.")
print("You start off with 5 points.")
print("Try to guess the number, but if you get it wrong you lose a point.")
print("However, you will get a hint.")
print("Good Luck!!!")
guess_the_number()