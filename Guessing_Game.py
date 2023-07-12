import random

def display_title():
    print("Guessing Game!")
    print()

def play_game(limit):
    number = random.randint(1, limit)
    print (f"I am thinking of a number from 1 to {limit}")
    count = 1
    guess = int(input("Enter the limit:     "))

    while(guess != number):
        if guess < number:
            print("Too Low.")
            count += 1
        elif guess > number:
            print("Too High.")
            count += 1
        guess = int(input("Guess Again:     "))
    print(f"You guessed it in {count}. \n")

def main():
    display_title()
    again = "yes"
    while again. lower() == "yes":
        limit = int(input("Enter the limit:     "))
        play_game(limit)
        again = input("Would you like to play again? (yes/no:   ")
        print()
    print("Thank for playing. Bye!")

if __name__ == "__main__":
    main()
