import random
import module

# random.randint(a, b) - returns a random integer where a <= number <= b

random_integer = random.randint(2, 25)
print(random_integer)

# To print a variable from a different file, use:
# file_name.variable_name
print(module.a)

# random.random() - returns random float where 0.0 <= number < 1.0
random_0_to_1 = random.random()
print(random_0_to_1)

#random.uniform(a, b) include b
random_float = random.uniform(0,1)
print(random_float)