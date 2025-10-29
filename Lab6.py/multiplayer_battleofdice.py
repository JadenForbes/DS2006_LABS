#multiplayer_battleofdice.py

import dice

print("Welcome to the Multiplayer Battle of Dices!")
print("Each player will roll ONE die: d6")

# Ask how many players
num_players = int(input("How many players? "))

# Nested list: [player_number, wins]
players = [[i + 1, 0] for i in range(num_players)]

# How many wins needed to become champion
win_goal = 3

while all(wins < win_goal for _, wins in players):
    input("\nPress ENTER to roll the dice for this round...")

    round_results = []

    # Each player rolls dice
    for player in players:
        player_num, _ = player
        roll = dice.roll_d6()
        round_results.append([player_num, roll])

        print(f"Player {player_num} rolled: d6={roll}")

    input("Press ENTER to see who won the round...")

    # Find highest roll in this round
    max_roll = max(total for _, total in round_results)
    winners = [player_num for player_num, total in round_results if total == max_roll]

    if len(winners) == 1:
        winner = winners[0]
        # Update winner’s score in players list
        for player in players:
            if player[0] == winner:
                player[1] += 1
        print(f"Player {winner} wins this round!")
    else:
        print("It's a tie between:", ", ".join([f"Player {w}" for w in winners]))

    # Print scores
    score_str = " | ".join([f"Player {p[0]}: {p[1]}" for p in players])
    print(f"Score → {score_str}")

# Determine final champion
champions = [p[0] for p in players if p[1] >= win_goal]
if len(champions) == 1:
    print(f"\n Player {champions[0]} is the Ultimate Battle of Dices Champion!")
else:
    print("\n It's a tie between:", ", ".join([f"Player {c}" for c in champions]))
