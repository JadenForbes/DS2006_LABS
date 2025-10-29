import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def __str__(self):
        return f"{self.name} (Wins: {self.wins})"


class Game:
    def __init__(self, players, win_goal=3, log_file="results.txt"):
        self.players = [Player(name) for name in players]
        self.win_goal = win_goal
        self.dice = Dice()
        self.round_number = 0
        self.log_file = log_file

        # Clear previous log file
        open(self.log_file, "w").close()

    def log_round(self, results):
        """Write round results to log file."""
        with open(self.log_file, "a") as f:
            result_str = ", ".join([f"{name} rolled {roll}" for name, roll in results.items()])
            f.write(f"Round {self.round_number}: {result_str}\n")

    def play_round(self):
        """Play a single round."""
        self.round_number += 1
        print(f"\n Round {self.round_number}")

        results = {}
        for player in self.players:
            roll = self.dice.roll()
            results[player.name] = roll
            print(f"{player.name} rolled a {roll}")

        # Determine winner(s)
        max_roll = max(results.values())
        winners = [p for p, r in results.items() if r == max_roll]

        if len(winners) == 1:
            winner = winners[0]
            for player in self.players:
                if player.name == winner:
                    player.wins += 1
            print(f" {winner} wins this round!")
        else:
            print("It's a tie between:", ", ".join(winners))

        # Log to file
        self.log_round(results)

    def show_scores(self):
        print("\n Current Scores:")
        for player in self.players:
            print(f"{player.name}: {player.wins} wins")

    def play_game(self):
        print("\n Welcome to the Ultimate Battle of Dices!")
        print("First to reach", self.win_goal, "wins becomes the Champion!\n")

        while all(p.wins < self.win_goal for p in self.players):
            input("Press ENTER to roll the dice...")
            self.play_round()
            self.show_scores()

        # Announce winner(s)
        champions = [p.name for p in self.players if p.wins >= self.win_goal]
        if len(champions) == 1:
            print(f"\n {champions[0]} is the Ultimate Champion!")
        else:
            print("\n It's a tie between:", ", ".join(champions))

        print(f"\nAll results saved to {self.log_file}.")


# ====== Main Function ======
def main():
    print("Welcome to the Ultimate Multiplayer Battle of Dices Setup!")
    num_players = int(input("How many players are playing? "))

    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        players.append(name)

    win_goal = int(input("Enter the number of wins needed to become Champion: "))

    # Start the game
    game = Game(players, win_goal)
    game.play_game()


# ====== Run Program ======
if __name__ == "__main__":
    main()
