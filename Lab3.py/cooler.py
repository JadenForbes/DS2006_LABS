# battle-of-dices-cooler.py

import dice

print("Welcome to the Cooler Battle of Dices!")
print("Each player will roll two different dice: d6 + d8")

player1_wins = 0
player2_wins = 0

while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")

    # Player 1 rolls
    p1_roll1 = dice.roll_d6()
    p1_roll2 = dice.roll_d8()
    p1_total = p1_roll1 + p1_roll2

    # Player 2 rolls
    p2_roll1 = dice.roll_d6()
    p2_roll2 = dice.roll_d8()
    p2_total = p2_roll1 + p2_roll2

    print(f"Player 1 rolled: d6={p1_roll1}, d8={p1_roll2} → Total = {p1_total}")
    print(f"Player 2 rolled: d6={p2_roll1}, d8={p2_roll2} → Total = {p2_total}")

    input("Press ENTER to continue...")

    if p1_total > p2_total:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif p2_total > p1_total:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("It's a tie!")

    print(f"Score: Player 1 - {player1_wins} | Player 2 - {player2_wins}")

if player1_wins == 3:
    print("Player 1 is the Ultimate Battle of Dices Champion!")
else:
    print("Player 2 is the Ultimate Battle of Dices Champion!")
