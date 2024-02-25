import random # Imports random module

num_1 = random.randint(0, 20) # Generates random integer within range [0, 20]
num_2 = random.randint(0, 20)

print(num_1)
print(num_2)

result = int(input("Write the sum: "))

if result != num_1 + num_2:
    print("Your are WRONG!")

else:
    print("You are CORRECT!")