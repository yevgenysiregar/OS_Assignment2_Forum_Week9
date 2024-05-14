import random

with open('requests.txt', 'w') as file:
    for _ in range(1000):
        file.write(f"{random.randint(0, 4999)}\n")