import random
import numpy as np
import statistics

random.seed(42)


# Function that returns win on the slot machine
def win():
    # 1 is Bar
    # 2 is bell
    # 3 is lemon
    # 4 is cherry
    random_number = [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)]
    if random_number == [1, 1, 1]:
        return 20
    elif random_number == [2, 2, 2]:
        return 15
    elif random_number == [3, 3, 3]:
        return 5
    elif random_number == [4, 4, 4]:
        return 3
    elif random_number[0] == 4 and random_number[1] == 4 and random_number[2] != 4:
        return 2
    elif random_number[0] == 4 and random_number[1] != 4 and random_number[2] != 4:
        return 1
    else:
        return 0


# function that plays the slot machine, until you run out of money
def slot_machine(coins):
    round_played = 0
    while coins >= 1:
        coins -= 1
        coins += win()
        round_played += 1
    return round_played


round_played = []

simulated_rounds = 100000

for i in range(simulated_rounds):
    round_played.append(slot_machine(10))

median = statistics.median(round_played)
mean = statistics.mean(round_played)

print(f"The simulation gives the median = {median} and the mean = {mean}")
