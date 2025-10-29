# battle-of-dices-better.py

import dice

print("Welcome to the Improved Battle of Dices!")

player1_wins = 0
player2_wins = 0

while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")

    player1_roll = dice.roll_d6()
    player2_roll = dice.roll_d6()

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    input("Press ENTER to continue...")

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif player2_roll > player1_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("It's a tie!")

    print(f"Score: Player 1 - {player1_wins} | Player 2 - {player2_wins}")

if player1_wins == 3:
    print("Player 1 is the Battle of Dices Champion!")
else:
    print("Player 2 is the Battle of Dices Champion!")
