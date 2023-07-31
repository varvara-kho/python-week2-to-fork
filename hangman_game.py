import random 
def choose_random_word():
    words = ["pizza", "starfish", "mountain", "sunshine", "guitar", "butterfly", "symphony"]
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
def hangman_game():
    print("Welcome to Hangman!")
    print("Rules of the game:")
    print("1. You need to guess the word letter by letter.")
    print(f"2. You have 9 attempts to guess the letters.\n")
    word = choose_random_word()
    guessed_letters = set()
    attempts = 9
    while attempts > 0:
        print("Word:", display_word(word, guessed_letters))
        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print("Incorrect! You have", attempts, "attempts left.")
    if "_" in display_word(word, guessed_letters):
        print("Game over. The word was:", word)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman_game()
    else:
        print("Thank you for playing Hangman!")
hangman_game()