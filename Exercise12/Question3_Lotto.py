import random

# Initialise an empty list to store 1-6
lotteryNumbers = []
#For loop, ("i"= integer (int))
for i in range(0, 6):
    number = random.randint(1, 50)
    # Check if this number has already been picked
    #While loop
    while number in lotteryNumbers:
        # if it has, pick a new number instead
        number = random.randint(1, 50)
    # we now have numbers to append to the list
    lotteryNumbers.append(number)
# Sort the list in ascending order
lotteryNumbers.sort()

print("The Lottery numbers are: ")
print(lotteryNumbers)

