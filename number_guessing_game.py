import random

def get_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy   (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard   (1 - 200)")

    while True:
        choice = input("Enter choice (1/2/3): ").strip()
        if choice == '1':
            return 50
        elif choice == '2':
            return 100
        elif choice == '3':
            return 200
        else:
            print("Invalid choice. Try again.")

def play_game(max_range):
    secret_number = random.randint(1, max_range)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_range}.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number.")

def main():
    best_score = None

    print("===== Number Guessing Game =====")

    while True:
        max_range = get_difficulty()
        attempts = play_game(max_range)

        # Update best score
        if best_score is None or attempts < best_score:
            best_score = attempts
            print("🔥 New Best Score!")

        print(f"🏆 Best Score (least attempts): {best_score}")

        # Replay option
        replay = input("\nDo you want to play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()