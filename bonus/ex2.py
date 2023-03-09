import random

upper_bound = int(input("Enter upper bound: "))
lower_bound = int(input("Enter lower bound: "))

random_number = random.randint(lower_bound, upper_bound)
print(f"Random number: {random_number}")
