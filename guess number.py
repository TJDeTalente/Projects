import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print(f"You guessed right! It was {random_number}!!")

        if guess > random_number:
            print("Too high")
        if guess < random_number:
            print("Too low")

def computer_guess(x):
    low = 1
    high = x
    feedback = ('')
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H) or too low (L), or correct (C)? ".lower())
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"We got a beat on you, you freak.")

computer_guess(100)




