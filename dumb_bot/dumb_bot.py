import random

def make_move(last_play, last_winner):
    if last_play == "R" and last_winner == "User":
        return random.choice(["Rock", "Paper", "Scissors", "Paper"])
    elif last_play == "P" and last_winner == "User":
        return random.choice(["Rock", "Scissors", "Paper", "Scissors"])
    elif last_play == "S" and last_winner == "User":
        return random.choice(["Rock", "Scissors", "Paper", "Rock"])
    elif last_play == "R" and last_winner == "Computer":
        return random.choice(["Rock", "Scissors", "Paper", "Rock"])
    elif last_play == "P" and last_winner == "Computer":
        return random.choice(["Rock", "Scissors", "Paper", "Paper"])
    elif last_play == "S" and last_winner == "Computer":
        return random.choice(["Rock", "Scissors", "Paper", "Scissors"])
    else:
        return random.choice(["Rock", "Paper", "Scissors"])