import random

def main():
    print("Welcome To The Number Guessing Game!")
    print("I Have Chosen A Random Number Between 1 And 100.")
    print("Try To Guess It Within 10 Attempts.\n")

    the_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter Your Guess: "))
        attempts += 1

        if guess < the_number:
            print("Too Low! Try Again.")
        elif guess > the_number:
            print("Too High! Try Again.")
        else:
            print(f"Congratulations...! You Guessed It Right In {attempts} Attempts.")
            break

        if attempts >= 10:
            print(f"Sorry, You've Reached The Maximum Number Of Attempts. The Correct Number Was {the_number}.")
            break

if __name__ == "__main__":
    main()
