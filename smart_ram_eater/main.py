from sam_altkey import make_move, learn, save_model_manually
import keyboard
import time
import sys
import random

history = []
last_winner = None
print("You are currently playing against a non-linear neuron")
time.sleep(0.9)
print("He trains from your every move")
time.sleep(1)
print("The more you play the smarter he gets...")
time.sleep(1.5)
print("Good luck!")
print("Click E to escape.")
while True:
    if len(history) >= 3:
        computer_move = make_move(history[-3], history[-2], history[-1], last_winner)
    else:
        computer_move = random.choice(["p", "r", "s"])

    user_play = input("Your move (R,P,S): ")
    if user_play.lower() == "r":
        move = "Rock"
    elif user_play.lower() == "p":
        move = "Paper"
    elif user_play.lower() == "s":
        move = "Scissors"
    else:
        move = "Invalid"
    computer_move = {
        "p": "Paper",
        "r": "Rock",
        "s": "Scissors"
    }[computer_move]
    if computer_move == "Paper" and move == "Rock" or computer_move == "Scissors" and move == "Paper" or computer_move== "Rock" and move == "Scissors" or move == "Paper" and computer_move == "Scissors":
        winner = "Computer"
    elif move == "Paper" and computer_move == "Rock" or move == "Scissors" and computer_move == "Paper" or move == "Rock" and computer_move == "Scissors" or move == "Scissors" and computer_move == "Paper":
        winner = "User"
    else:
        winner = "Draw"
    if len(history) >= 3:
        learn(history[-3], history[-2], history[-1], user_play)

    history.append(user_play.lower())
    history = history[-3:]

    last_winner = winner
    print(f"""
    Your move:
    {
    move
    }
    Computer move:
    {
    computer_move
    }
    Winner:
    {winner}
    """
    )
    if keyboard.is_pressed("e"):
        save_model_manually()
        time.sleep(0.1) # just to be safe
        sys.exit()