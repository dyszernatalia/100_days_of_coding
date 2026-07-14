import random 

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_pick = random.randint(0, len(friends)-1)

print(f"Today pays: {friends[random_pick]}")

#another option
print(f"Today pays: {random.choice(friends)}")