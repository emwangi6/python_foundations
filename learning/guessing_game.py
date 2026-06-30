# a guessing game
import random
randomnumber = random.randint(1, 100)
attempt =0

while True:
    print("Guess an number between 1 and 100 (You have 3 attempts)")
    guess = int(input('>'))
    if guess != randomnumber and attempt >= 2:
        print("Out of attempts")
        print(f'Correct answer was {randomnumber}')
        break
    if guess < randomnumber:
        print("Too low. Try again")
        attempt += 1
        continue
    elif guess > randomnumber:
        print("Too high. Try again")
        attempt += 1
        continue
    else:
        print("You guessed right!")
        print(f"You guessed {attempt +1 } times.")
        break

