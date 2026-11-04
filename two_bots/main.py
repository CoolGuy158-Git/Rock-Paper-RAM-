from smart_ram_eater.sam_altkey import make_move as make_a_smart_move, learn, save_model_manually
from dumb_bot.dumb_bot import make_move
import random
import keyboard
import sys
import time

history = []
last_winner = None
amount = 0
winners = []
while True:
    if len(history) >= 3:
        computer_move = make_a_smart_move(history[-3], history[-2], history[-1], last_winner)
    else:
        computer_move = random.choice(["p", "r", "s"])

    if len(history) > 0:
        user_play = make_move(last_winner, history[-1])
        if user_play == "Rock":
            user_play = "R"
        elif user_play == "Paper":
            user_play = "P"
        else:
            user_play = "S"
    else:
        user_play = make_move(last_winner, None)
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
        winner = "Smart wins"
    elif move == "Paper" and computer_move == "Rock" or move == "Scissors" and computer_move == "Paper" or move == "Rock" and computer_move == "Scissors" or move == "Scissors" and computer_move == "Paper":
        winner = "Dumb wins"
    else:
        winner = "Draw"
    if len(history) >= 3:
        learn(history[-3], history[-2], history[-1], user_play, last_winner)

    history.append(user_play.lower())
    history = history[-3:]

    last_winner = winner

    amount += 1
    if winner == "Smart wins":
        winners.append(1)
    elif winner == "Dumb wins":
        winners.append(2)
    else:
        winners.append(3)
    if amount % 100 == 0:
        smart_amount = winners.count(1)
        dumb_amount = winners.count(2)
        if smart_amount > dumb_amount:
            overall_winner = "Smart"
        elif smart_amount < dumb_amount:
            overall_winner = "Dumb"
        else:
            overall_winner = "Draw"
        print(f"Epoch: {amount} | Winner this epoch: {winner} | Overall winner: {overall_winner}")
        print(f"Amount of wins for smart: {smart_amount}")
        print(f"Amount of wins for dumb: {dumb_amount}")
        winners.clear()
    if keyboard.is_pressed("e"):
        save_model_manually()
        time.sleep(0.1) # just to be safe
        sys.exit()