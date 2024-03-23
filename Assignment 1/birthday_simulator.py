import numpy as np
import statistics
import random
import matplotlib.pyplot as plt
import bisect

# seeds the random number generator
random.seed(42)


# Function that runs one simulation of N people, and check if someone has the same birthday
def same_birthday(N):
    birthdays = []
    for i in range(N):
        birthdays.append(random.randint(1, 365))

    seen_number = set()
    has_duplicate = False
    for number in birthdays:
        if number in seen_number:
            has_duplicate = True
            break
        seen_number.add(number)

    return has_duplicate


# Function that runs multiple simulation of same_birthday simulation, and
# Return the percentage of the simulations where they have the same birthday
def simulating_birthdays(N, Simulations):
    true_or_false = []
    for x in range(Simulations):
        true_or_false.append(same_birthday(N))
    # Calculate the percentage of True values
    percentage_true = (sum(true_or_false) / len(true_or_false)) * 100

    return percentage_true


percentage_interval = []

for x in range(10, 50):
    percentage_interval.append(simulating_birthdays(x, 1000))

x_axis = np.linspace(10, 50, num=40)

print("exercise 3, Part 1")
print(f"Smallest number of N where the probability of the event occurring "
      f"is {10 + bisect.bisect_left(percentage_interval, 50)} \n")

plt.plot(x_axis, percentage_interval)
plt.axhline(50, color="red", label="50% chance")
plt.legend()
plt.show()


def every_day_birthday():
    days_covered = set()
    group_size = 0
    while len(days_covered) < 365:
        new_birthday = random.randint(1, 365)
        if new_birthday not in days_covered:
            days_covered.add(new_birthday)
        else:
            pass
        group_size += 1

    return group_size

def mean_finder(sim):
    number_days = []
    for i in range(sim):
        number_days.append(every_day_birthday())
    mean_value = statistics.mean(number_days)
    return mean_value


print("Exercise 3 Part 2")
print(f"expected size of Peters group is {mean_finder(2000)},"
      f" (after 2000) simulations")

