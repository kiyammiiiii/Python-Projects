import random

SIGNS = [ROCK, PAPER, SCISSORS] = ["rock", "paper", "scissors"]

def get_random_sign():
    return random.choice(SIGNS)

def battle_status(health):
    return "Health: " + "*" * health

def get_points(points):
    return f"Total Points: {points}"

def main():

    health = 5
    points = 0

    print("Welcome to the Rock, Paper, Scissors Game!")
    while True:
        print(battle_status(health))
        user_input = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()
        if user_input == "quit":
            print(get_points(points))
            print("Thanks for playing! Goodbye!")
            break
        elif user_input not in SIGNS:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_random_sign()
        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
            points += 1
        elif (user_input == ROCK and computer_choice == SCISSORS) or \
             (user_input == PAPER and computer_choice == ROCK) or \
             (user_input == SCISSORS and computer_choice == PAPER): 
            print("You win!")
            points += 2
        else:
            print("You lose!")
            health -= 1
            points = max(points - 1,  0)
        print(get_points(points))
        if health <= 0:
            print("Game over! You ran out of health.")
            break


main()