import random
min = 1
max = 6

pick = input("Pick a number 1-6: ")

print("Rolling die...")

dice = random.randint(min, max)
print (dice)

if pick == dice:
    print ("You guessed Correctly!")
else:
    print ("Wrong Guess")

