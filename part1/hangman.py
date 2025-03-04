import random
# get a word from a list and output it as a series of blanks
# make the player guess a letter if the word has occurences of the letter change the blank word to reveal those particular blanks into the letters
#repeat until all blanks are gone


Hangman_words = ["mistborn", "stormlight", "calamity", "elantris", "librarian", "odium", "honor", "trell", "silence", "starsight", "warbreaker", "emerald", "rythm", "scriviner"]
rand_word = random.choice(Hangman_words)
word = list(rand_word)
secret_word = "".join(word)
hidden_word = []
lives = 6


word_count = len(word)
print("Welcome to Hangman!")



while word_count > 0:
    hidden_word += "_"
    word_count -= 1


# print(hidden_word)
# print(word)
completed = "".join(hidden_word)
print(completed)

def game_over():
    
    if all(i == "_" for i in word):
        print("Congratulations! you won!")
    elif lives == 0:
        print("Game over, you lost")
        print(f"The word was {secret_word}")
    else:
        make_guess()
        


def make_guess():
    global lives    

    # find a letter
    guess = input("guess a letter!\n")
    # check if letter is in the guess and how many times
    check = word.count(guess)


    # if the letter is in the word find the index position of the letter and replace the blank words letters with the guessed letter
    if guess in word:
        for letter in range(0, check):
            # find the letter postions
            found = word.index(guess)

            # replace the blank positons with the guess
            hidden_word[found] = guess

            # clear the words index so it doesnt change the same letter multiple times
            word[found] = "_"

    else:
        print("Not in word")
        lives -= 1
        print(f"You have {lives} lives remaining")



    completed = "".join(hidden_word)
    print(completed)

    game_over()


    # print(hidden_word)
    # print(word)


make_guess()



#    o
#   /|\
#   / \
