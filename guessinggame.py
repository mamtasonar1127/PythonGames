answer = 5

print("Please guess number between 1 to 10:")
guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess low")
else:
    print("You got it first time")