from dumb_bot import make_move

last_play = None
last_winner = None
while True:
    user_play = input("Your move (R,P,S): ")
    last_play = user_play
    computer_move = make_move(last_play, last_winner)
    if user_play.lower() == "r":
        move = "Rock"
    elif user_play.lower() == "p":
        move = "Paper"
    elif user_play.lower() == "s":
        move = "Scissors"
    else:
        move = "Invalid"

    if computer_move == "Paper" and move == "Rock" or computer_move == "Scissors" and move == "Paper" or computer_move== "Rock" and move == "Scissors" or move == "Paper" and computer_move == "Scissors":
        winner = "Computer"
    elif move == "Paper" and computer_move == "Rock" or move == "Scissors" and computer_move == "Paper" or move == "Rock" and computer_move == "Scissors" or move == "Scissors" and computer_move == "Paper":
        winner = "User"
    else:
        winner = "Draw"
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
