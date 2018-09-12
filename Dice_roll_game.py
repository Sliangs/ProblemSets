import random

def roll(sides):

    rand_roll = int(random.randint(1, sides))
    print("you have rolled a ", rand_roll)
    return rand_roll


def main():
    sides = 6
    rolling = True

    while rolling:
        answer = input("do you want to roll 6-sided die? (y/n)   ")
        if answer.lower() == 'y':
            die = int(input("enter the amount of dice you wish to roll (max 6): "))
            combo = []
            for value in range(1,die):
                combo.append(roll(sides))
            print("you have rolled a Total value of: ", sum(combo))
            break



        else:
            print("Thank you for playing!")
            break

main()


