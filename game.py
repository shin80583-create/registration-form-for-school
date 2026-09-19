import random

secret_number = random.randint(1, 20)
attempts = 0

def new_game():
    global secret_number, attempts
    secret_number = random.randint(1, 20)
    attempts = 0

def check_guess(guess):
    global attempts
    attempts += 1
    if guess < secret_number:
        return "⬆️ Too low! Try again."
    if guess > secret_number:
        return "⬇️ Too high! Try again."
    return f"🎉 Correct! You got it in {attempts} tries. Press New Game to play again."
