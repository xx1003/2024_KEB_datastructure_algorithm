import random

ans = random.randint(1, 100)
chance = 7

while chance != 0:
    x = int(input("Input guess number : "))
    if x == ans:
        print(f"You win. Answer is {ans}.")
        print(chance)
        break
    elif x < ans:
        print(f"{x} is smaller. Chance left : {chance}")
        chance -= 1
    else:
        print(f"{x} is bigger. Chance left : {chance}")
        chance -= 1
else:
    print(f"You lost. Answer is {ans}.")