import random 

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_pick = random.randint(0, len(friends)-1)

print(f"today pays: {friends[random_pick]}")