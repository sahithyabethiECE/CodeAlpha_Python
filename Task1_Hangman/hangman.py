import random

def choose_word():
    """from Word list  random  word is  pickedc """
    words = ["python", "coding", "laptop", "hangman", "program", "intern", "github", "english"]
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    """Guessed letters will be shown, remaining will be shown as '_'"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_hangman(tries):
    """when Tries decrease hangman figure will be drawn """
    stages = [
        """
           |
           | O
           | \\|/
           | |
           | / \\
           -
        """,
        """
           |
           | O
           | \\|/
           | |
           | / 
           -
        """,
        """
           |
           | O
           | \\|/
           | |
           | 
           -
        """,
        """
           |
           | O
           | \\|
           | |
           | 
           -
        """,
        """
           |
           | O
           | |
           | |
           | 
           -
        """,
        """
           |
           | O
           | 
           | 
           | 
           -
        """,
        """
           |
           | 
           | 
           | 
           | 
           -
        """ # <-- closed this properly
    ]
    return stages[tries]

# Example usage
def play_game():
    word = choose_word()
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman ")
    
    while tries > 0:
        print(display_hangman(tries))
        print("Word:", display_word(word, guessed_letters))
        print("Guessed letters:", ' '.join(guessed_letters))
        
        guess = input("guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("Already guessed!")
            continue
            
        guessed_letters.append(guess)
        
        if guess not in word:
            tries -= 1
            print(f"Wrong ! {tries} tries remaining")
        
        if all(letter in guessed_letters for letter in word):
            print("Word:", word)
            print("Super , uh have won ! 🎉")
            break
    else:
        print(display_hangman(tries))
        print(f"Game over. Word is: {word}")

if __name__ == "__main__":
    play_game()
