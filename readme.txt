**Wordle in Python**

A basic command-line version of the classic Wordle game, built in Python! 
This version works on both Linux and Windows systems.

**Features**

- Random word selection from a list of words stored in `.txt` files.
- Ability to choose words of different lengths (3 to 8).
- Validates guesses and gives feedback:
  - One line will show all the correct letters entered in arbitrary order.
  - Another line will list all the letters that aren't present in the word.
  - Another line will show you the letters in the correct order as you get them right.
- Cross-platform (tested on Linux and Windows).

**Setup**

1. Clone the repository:


   git clone https://github.com/salvageme/wordle.git
   
   cd wordle
   


2. Make sure you have Python 3 installed:

You can check with:

    python --version
or
    python3 --version


3. Run the game:

    python wordle.py
Or:
    python3 wordle.py


**File Structure**

   -  wordle.py – The main game file
   -  words – Folder that contains all the words

Make sure the words folder is in the same directory as wordle.py.


**How to Play**

    Start the game.
    
    select the number of letter you want.

    You have 6 attempts to guess the word.

    After each guess, you'll receive feedback.

    Use that feedback to narrow down your next guess!


**License**

This project is licensed under the MIT License.

Have fun playing Wordle in your terminal!
