import random

gallows = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
    ]



        word_list = ["wilson", "parker", "oreo", "project", "homework", "college"]
        word_list = [x.upper() for x in word_list]

        word = word_list[random.randrange(8)]
        word_letters = []
        guessed_letters = []
        incorrect_guess = 0
        hangman_level = 0
        done = False
        for i in range(len(word)):
            print("_ ", end="")

    while not done:
        print(gallows[hangman_level])
        correct_guesses = 0
        letters_remaining = len(word)
        guess = input("\nPick a letter: ")
        if guess.lower() in guessed_letters:
            print("You have already guessed that letter. Pick another one.")
        if guess.lower() not in guessed_letters:
            guessed_letters.append(guess)
        if guess.lower() in word.lower():
            if guess.lower() not in guessed_letters:
                correct_guesses += 1
            word_letters.append(guess.lower())
        else:
            incorrect_guess += 1
            hangman_level += 1
        for letter in word.lower():
            if letter in word_letters:
                print(letter + " ", end="")
                letters_remaining -= 1
            else:
                print("__", end=" ")

        if incorrect_guess >= 6:
            print("You LOSE")
            done = True

        if letters_remaining == 0:
            done = True
            print("You have won! Want to play again?")









