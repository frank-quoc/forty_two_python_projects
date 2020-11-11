from random import randint

def dice_roll():
    repeat = True

    while repeat:
        res = randint(1,6)
        print("You rolled", res)
        repeat = ("y" or "yes") in input("Do you want to roll again? ").lower()

if __name__ == '__main__':
    dice_roll()
