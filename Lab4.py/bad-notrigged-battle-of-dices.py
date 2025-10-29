import dice

# Dice options mapped to their function names
DICE_OPTIONS = {
    "d4": dice.roll_d4,
    "d6": dice.roll_d6,
    "d8": dice.roll_d8,
    "d12": dice.roll_d12,
    "d20": dice.roll_d20,
    "d100": dice.roll_d100
}

print("Welcome to the Cooler Battle of Dices (Custom Dice Edition)!")
print("You will choose ONE dice type to roll each round.")

# Ask player 1 for their dice choice
while True:
    player1_choice = input("Player 1, choose your dice (d4, d6, d8, d12, d20, d100): ").lower()
    if player1_choice in DICE_OPTIONS:
        break
    print("Invalid choice. Please try again.")

# Ask player 2 for their dice choice
while True:
    player2_choice = input("Player 2, choose your dice (d4, d6, d8, d12, d20, d100): ").lower()
    if player2_choice in DICE_OPTIONS:
        break
    print("Invalid choice. Please try again.")

# Get the roll functions
player1_roll_func = DICE_OPTIONS[player1_choice]
player2_roll_func = DICE_OPTIONS[player2_choice]

# Initialize scores and history
player1_wins = 0
player2_wins = 0
round_number = 1

player1_rolls = []
player2_rolls = []

# Game loop
while player1_wins < 3 and player2_wins < 3:
    input(f"\n Round {round_number} - Press ENTER to roll...")

    p1_roll = player1_roll_func()
    p2_roll = player2_roll_func()

    player1_rolls.append(p1_roll)
    player2_rolls.append(p2_roll)

    print(f" Player 1 rolled a {player1_choice.upper()}: {p1_roll}")
    print(f" Player 2 rolled a {player2_choice.upper()}: {p2_roll}")

    if p1_roll > p2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
    elif p2_roll > p1_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
    else:
        print("It's a tie!")

    print(f"Score → Player 1: {player1_wins} | Player 2: {player2_wins}")
    round_number += 1

# End of Game
print("\n Game Over!")
if player1_wins == 3:
    print("Player 1 is the Ultimate Battle of Dices Champion!")
else:
    print(" Player 2 is the Ultimate Battle of Dices Champion!")

# Summary Table
print("\n Final Summary - Round by Round:")
print("-----------------------------------------------------")
print("| Round | P1 Dice | P1 Roll || P2 Dice | P2 Roll |")
print("-----------------------------------------------------")
for i in range(len(player1_rolls)):
    print(f"| {i+1:^5} | {player1_choice.upper():^7} | {player1_rolls[i]:^8} || {player2_choice.upper():^7} | {player2_rolls[i]:^8} |")
print("-----------------------------------------------------")
# Ask user for file name
file_name = input("\n Enter a file name to save the summary (e.g., summary.txt): ")

# Build summary as a string
summary = ""
summary += "\n Final Summary - Round by Round:\n"
summary += "---------------------------------------------\n"
summary += "| Round     |"
for i in range(len(player1_rolls)):
    summary += f" {i+1} |"
summary += "\n---------------------------------------------\n"

summary += "| Player 1  |"
for roll in player1_rolls:
    summary += f" {roll} |"
summary += "\n"

summary += "| Player 2  |"
for roll in player2_rolls:
    summary += f" {roll} |"
summary += "\n---------------------------------------------\n"

# Save to file
try:
    with open(file_name, "w") as file:
        file.write(summary)
    print(f"Summary saved successfully to '{file_name}'")
except Exception as e:
    print(f"Failed to save file: {e}")
