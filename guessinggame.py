import random

highest = 10
answer = random.randint(1, highest)
guess = 0  # initialize to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done , you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
      #  guess = int(input())
      #  if guess == answer:
      #      print("Well done, you guessed it")
      #  else:
      #      print("Sorry, you have not guessed correctly")
