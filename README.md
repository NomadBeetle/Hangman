# 📝 Hangman Game

A simple command-line Hangman game built with Python.

## 🎮 How to Play
1. The program randomly selects a word.
2. You guess letters one at a time.
3. If the guessed letter is correct, it's revealed in the word.
4. If it's incorrect, you lose a life.
5. Keep guessing until you complete the word or run out of lives.

## 🛠 Installation & Setup
### Prerequisites
- Python 3.x installed

### Running the Game
Clone the repository and run:
```sh
git clone https://github.com/NomadBeetle/Hangman.git
cd Hangman
python main.py
```

## 📂 Project Structure
```
/hangman-game
│── hangman_art.py
│── hangman_words.py
│── main.py
│── README.md
│── .gitignore
```

## 📜 Features
- Random word selection
- Lives system for incorrect guesses
- ASCII art for a fun visual experience
- Input validation for repeated guesses