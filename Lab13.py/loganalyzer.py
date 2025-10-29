import pandas as pd

class LogAnalyser:
    def __init__(self):
        self.data = []
        self.player_names = []
        self.df = pd.DataFrame()

    def load_log_file(self, filename):
        """Reads a Battle of Dices log file and loads it into a pandas DataFrame."""
        with open(filename, "r") as file:
            lines = file.readlines()

        rounds = []
        for line in lines:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            # Example line: "Round 1: a rolled 3, b rolled 1, c rolled 6"
            parts = line.split(": ")[1]  # get the part after "Round X:"
            rolls = parts.split(", ")

            round_data = {}
            for roll in rolls:
                player, value = roll.split(" rolled ")
                round_data[player] = int(value)

                if player not in self.player_names:
                    self.player_names.append(player)

            rounds.append(round_data)

        # Convert list of dicts into DataFrame
        self.df = pd.DataFrame(rounds)
        print("✅ Log file successfully loaded into DataFrame!")
        print(self.df)
analyser = LogAnalyser()
analyser.load_log_file("Lab13.py/results.txt")
