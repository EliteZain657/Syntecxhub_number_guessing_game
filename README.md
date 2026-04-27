🎯 Number Guessing Game (CLI)

A simple yet structured command-line Number Guessing Game built in Python. The project focuses on core programming fundamentals such as loops, conditionals, functions, and random number generation, while also incorporating user interaction and basic game state tracking.

📌 Overview

The program generates a random number within a selected range based on difficulty level. The player attempts to guess the number, receiving feedback ("too high" or "too low") after each attempt. The game tracks the number of attempts and maintains the best (lowest) score during the session.

🚀 Features
Random number generation using Python’s random module
Multiple difficulty levels:
Easy (1–50)
Medium (1–100)
Hard (1–200)
Real-time hints (higher/lower feedback)
Attempt counter for each round
Best score tracking (lowest attempts)
Replay option after each game
Input validation with error handling
Modular design using functions
🧠 Concepts Demonstrated

This project is designed to reinforce fundamental programming concepts:

Loops (while loops for continuous gameplay)
Conditional statements (if-elif-else for decision making)
Functions (code modularization)
Exception handling (try-except for input validation)
Random number generation (random.randint)
State management (tracking attempts and best score)
🛠️ How to Run
Ensure Python is installed on your system
Download or clone the repository
Navigate to the project directory

Run the script using:

python guess_game.py

🎮 Gameplay Instructions
Choose a difficulty level
The system selects a random number within the chosen range
Enter your guesses
Receive hints after each attempt
Continue until you guess correctly
View your attempt count and best score
Choose whether to play again
📈 Example Flow
User selects Medium difficulty (1–100)
System generates a number (e.g., 73)
User guesses:
50 → Too low
80 → Too high
73 → Correct
Game displays total attempts and updates best score
🔧 Possible Enhancements
Persist best score using a file (JSON or text)
Add attempt limits per difficulty level
Implement scoring system based on efficiency
Add time tracking for each round
Build a graphical user interface (GUI) using Tkinter
Add unit tests for better software quality assurance
📚 Purpose

This project is ideal for beginners and intermediate learners aiming to strengthen core Python skills and understand structured program design. It is also suitable as a small portfolio or internship-level project demonstrating clean logic and user interaction handling.

🏁 Conclusion

The Number Guessing Game is a compact yet effective way to practice essential programming constructs while building something interactive. It serves as a foundation for more advanced game logic, UI development, and persistent data handling.# Syntecxhub_number_guessing_game
