# 📘 Assignment: Hangman Game

## 🎯 Objective

Practice string manipulation, loops, conditionals, and random selection by building the classic Hangman word-guessing game.

## 📝 Tasks

### 🛠️ Word Selection and Game State Setup

#### Description
Write the setup code that randomly selects a secret word and initializes the variables needed to track the player's progress.

#### Requirements
Completed program should:

- Randomly select a word from the `words` list using the `random` module.
- Keep track of the letters guessed so far.
- Keep track of the number of incorrect guesses made.
- Define a maximum number of incorrect guesses allowed before the game ends.

### 🛠️ Main Game Loop

#### Description
Write the main loop that lets the player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Display the current progress of the secret word, showing guessed letters and underscores for unguessed letters (e.g., `_ y t h _ n`).
- Prompt the player to guess a single letter using `input()`.
- Check if the guessed letter is in the secret word:
  - If correct, reveal the letter in the displayed progress.
  - If incorrect, increase the count of incorrect guesses.
- Repeat until the word is fully guessed or the maximum number of incorrect guesses is reached.

### 🛠️ Win/Lose Messages

#### Description
Write the code that displays the final outcome of the game once the loop ends.

#### Requirements
Completed program should:

- Print a win message if the player reveals the entire word before running out of attempts.
- Print a lose message showing the secret word if the player runs out of attempts.
- Example output:
  ```
  You guessed the word: python
  You win!
  ```
  ```
  Out of attempts! The word was: python
  You lose!
  ```
