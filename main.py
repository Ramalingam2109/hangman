import random

WORDS = ["python", "programming", "hangman", "challenge", "developer", "algorithm"]


def choose_random_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# def play_again(score, failed_attempts):
#     """Ask the player if they want to play another game."""
#     choice = input("Enter Y or Enter to play again :").lower().strip()
#     if choice != "y" and choice != "":
#         print(f"You have scored {score} in {score + failed_attempts}")
#         return False
#     return True

def play_again(score, failed_attempts):
    """Ask the player if they want to play another game."""
    choice = input("Enter Y or Enter to play again, or any other key to quit: ").lower().strip()
    if choice != "y" and choice != "":
        print(f"You have scored {score} in {score + failed_attempts} games.")
        return False
    return True


def get_player_input(guessed_letters):
    # while loop for avoiding existing letters and numbers
    while True:
        guess = input("Enter a letter to guess :").lower().strip()
        if guess not in guessed_letters:

            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Enter a valid single alphabhet .")
        else:
            print("This letter is aldready guessed .")


def play_game():
    user_name = input("Enter your name :")
    # used for replaying the game without exiting .....
    game = True
    failed_attempts = 0
    score = 0

    while game:
        print(f"Welcome to hangman {user_name}")
        
        word = choose_random_word()
        attempts = 6
        guessed_letters = set()

        while attempts > 0:
            print(display_word(word, guessed_letters))

            player_guess = get_player_input(guessed_letters)
            guessed_letters.add(player_guess)

            if player_guess not in word:
                attempts -= 1
                print(f"The word has {len(word)} letters. You have {attempts} attempts to guess it.")
                if attempts == 0:

                    print(f"Total guesses ended user {user_name}.")
                    failed_attempts += 1
                    print(f"The word was {word}")
                    print(
                        f"Your score is {score} ,failed {failed_attempts} Wanna Try another time "
                    )
                    break
                    if not play_again(score, failed_attempts):
                        game = False
                break

            else:
                print("Correct Guess ")

            # print(current_display)

            
            if "_" not in display_word(word, guessed_letters):
                print(f"Congratulations, you won, {user_name}!")
                score += 1
                print(f"Your score is {score}, do u want to try again ? ")
                if not play_again(score, failed_attempts):
                    game = False
                    break
                break


if __name__ == "__main__":
    play_game()
