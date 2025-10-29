# battle-of-dices-multiplayer.py

import dice

print("Welcome to the Multiplayer Battle of Dices!")
print("Each player will roll two different dice: d6 + d8")

# Ask how many players
number_of_players = int(input("How many players? "))

# Player template
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0
}

players = []

# For loop to obtain the player names (FIGURE 1 style: .copy())
for i in range(number_of_players):
    player = player_info.copy()

    player["name"] = input(f"What is the name of Player {i+1}? ")
    player["email"] = input(f"What is the e-mail of Player {i+1}? ")
    player["country"] = input(f"What is the country of Player {i+1}? ")

    players.append(player)

# How many wins needed to become champion
win_goal = 3

while all(player["wins"] < win_goal for player in players):
    input("\nPress ENTER to roll the dice for this round...")

    round_results = []

    # Each player rolls dice
    for player in players:
        roll1 = dice.roll_d6()
        roll2 = dice.roll_d8()
        total = roll1 + roll2
        round_results.append({"name": player["name"], "total": total})

        print(f"{player['name']} rolled: d6={roll1}, d8={roll2} → Total = {total}")

    input("Press ENTER to see who won the round...")

    # Find highest roll in this round
    max_total = max(result["total"] for result in round_results)
    winners = [result["name"] for result in round_results if result["total"] == max_total]

    if len(winners) == 1:
        winner_name = winners[0]
        for player in players:
            if player["name"] == winner_name:
                player["wins"] += 1
        print(f"{winner_name} wins this round!")
    else:
        print("It's a tie between:", ", ".join(winners))

    # Print scores
    score_str = " | ".join([f"{player['name']}: {player['wins']}" for player in players])
    print(f"Score → {score_str}")

# Determine final champion
champions = [player["name"] for player in players if player["wins"] >= win_goal]
if len(champions) == 1:
    print(f"\n{champions[0]} is the Ultimate Battle of Dices Champion!")
else:
    print("\nIt's a tie between:", ", ".join(champions))
