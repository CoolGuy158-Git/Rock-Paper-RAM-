import random
import os

filename = "model.txt"

if os.path.exists(filename):
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("W1: "):
                weight1 = float(line.removeprefix("W1: "))
            elif line.startswith("W2: "):
                weight2 = float(line.removeprefix("W2: "))
            elif line.startswith("W3: "):
                weight3 = float(line.removeprefix("W3: "))
            elif line.startswith("B: "):
                bias = float(line.removeprefix("B: "))
else:
    weight1 = random.uniform(0.8, 1.2)
    weight2 = random.uniform(0.8, 1.2)
    weight3 = random.uniform(0.8, 1.2)
    bias = random.uniform(-0.2, 0.2)
learn_rate = 0.09
def make_move(first_last_play, second_last_play, third_last_play, last_winner):
    global bias, weight1, weight2, weight3
    first_tokens = 0
    second_tokens = 0
    third_tokens = 0
    if last_winner == "User" or last_winner == "Dumb wins": # Realized this never works in the two bots arena so just added an or
        add = 0.01
    else:
        add = 0.02
    if first_last_play.lower() == "p":
        first_tokens = 1 + add
    elif first_last_play.lower() == "r":
        first_tokens = 2 + add
    elif first_last_play.lower() == "s":
        first_tokens = 3 + add

    if second_last_play.lower() == "p":
        second_tokens = 1 + add
    elif second_last_play.lower() == "r":
        second_tokens = 2 + add
    elif second_last_play.lower() == "s":
        second_tokens = 3 + add

    if third_last_play.lower() == "p":
        third_tokens = 1 + add
    elif third_last_play.lower() == "r":
        third_tokens = 2 + add
    elif third_last_play.lower() == "s":
        third_tokens = 3 + add
    # Ts my first time trying a non-linear thing
    # Basically the equation is output = max(0, (x1 × w1) + (x2 × w2) + (x3 × w3) + b)
    # It uses a ReLU activation
    raw_output_token = first_tokens * weight1 + second_tokens * weight2 + third_tokens * weight3 + bias
    output_token = max(0, raw_output_token)

    predicted_token = min(
        [1, 2, 3],
        key=lambda n: abs(output_token - n)
    )

    return {1: "p", 2: "r", 3: "s"}[predicted_token]

def learn(first_player_input, second_player_input, third_player_input, actual_next_play, last_winner):
    global weight1, weight2, weight3, learn_rate, bias

    if last_winner == "User" or last_winner == "Dumb wins": # Realized this never works in the two bots arena so just added an or
        add = 0.01
    else:
        add = 0.02
    # Add reinforcement(yyy) learning
    if last_winner == "User" or last_winner == "Dumb wins":
        reward = -2.0
    elif last_winner == "Computer" or last_winner == "Smart wins":
        reward = 2.0
    else:
        reward = -0.5
    # Fixed inconsistency in train and learn by adding ts
    first_token = 0
    second_token = 0
    third_token = 0
    if first_player_input.lower() == "p":
        first_token = 1 + add
    elif first_player_input.lower() == "r":
        first_token = 2 + add
    elif first_player_input.lower() == "s":
        first_token = 3 + add

    if second_player_input.lower() == "p":
        second_token = 1 + add
    elif second_player_input.lower() == "r":
        second_token = 2 + add
    elif second_player_input.lower() == "s":
        second_token = 3 + add

    if third_player_input.lower() == "p":
        third_token = 1 + add
    elif third_player_input.lower() == "r":
        third_token = 2 + add
    elif third_player_input.lower() == "s":
        third_token = 3 + add

    target = {"p": 1, "r": 2, "s": 3}[actual_next_play.lower()]

    raw_prediction = first_token * weight1 + second_token * weight2 + third_token * weight3 + bias
    prediction = max(0, raw_prediction)
    error = target - prediction

    weight1 += learn_rate * error * first_token + reward * first_token
    weight2 += learn_rate * error * second_token + reward * second_token
    weight3 += learn_rate * error * third_token + reward * third_token
    bias += learn_rate * error

    with open("model.txt", "w") as file:
        file.write(f"W1: {weight1}\nW2: {weight2}\nW3: {weight3}\nB: {bias}")
def save_model_manually():
    with open("model.txt", "w") as file:
        file.write(f"W1: {weight1}\nW2: {weight2}\nW3: {weight3}\nB: {bias}")