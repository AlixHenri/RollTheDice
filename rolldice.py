import random

def roll_dice():
    roll = input("Do you want to roll the dice? (Yes/No): ").upper()

    if roll == "YES" or roll == "Y":
        dice1 = random.randint(1,6)
        print(f'First dice rolled: {dice1}')
        roll_again = input('Do you want to roll another dice? (Yes/No): ').upper()

        if roll_again == "YES" or roll_again == 'Y':
            dice2 = random.randint(1,6)
            total = dice1 + dice2
            print(f"Second dice rolled: {dice2}")
            print(f'Total: {total}')
        else:
            print(f'Total {dice1}')
            print('Bye! :)')

    else:
        print('Okay, bye! :)')
        quit()

roll_dice()