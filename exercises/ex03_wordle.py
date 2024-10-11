"""Wordle exercise!"""

__author__ = "730766709"


def input_guess(word_val: int) -> str:
    """Guess a word"""
    word: str = input(f"Enter a {word_val} character word: ")
    while len(word) != word_val:
        word = input(f"That wasn't {word_val} chars! Try again:")
    return word


# kept getting errors here, had if statement, but comp110 suggest loop. figured it out!


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks for char in word"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


# idk how to return T/F when return type is bool. I could do it with None return type
# eventually figured out, simplified


def emojified(guess: str, secret: str) -> str:
    """Wordle emoji colors for letters"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    check: str = ""
    index: int = 0
    while index < len(secret):
        if secret[index] == guess[index]:
            check += GREEN_BOX
        elif contains_char(secret, guess[index]):
            check += YELLOW_BOX
        else:
            check += WHITE_BOX
        index += 1
    return check


# was getting boxes vertical at first, then would only get two colors
# don't fully understand what i have done


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False  # player loses
    while turn <= 6 and win == False:
        print(f"===Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            win = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
