import random

input("Press Enter to toss a coin! ")

coin_toss = random.randint(0,1)

if coin_toss == 0:
    print("Heads")
else:
    print("Tails")

