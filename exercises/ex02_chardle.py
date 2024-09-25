"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730766709"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        print(word)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


# had to look back at other practice code/in class code to do this


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        print(letter)
    else:
        print("Error: Character must be a single character.")
        exit()
    return letter


# had to look back at other practice code/in class code to do this


def contains_char(word: str, letter: str) -> None:
    index: int = 0
    count: int = 0
    print("Searching for " + str(letter) + " in " + str(word))
    while index < len(word):
        if word[index] == letter:
            print(str(letter) + " found at index " + str(index))
            count += 1
        index += 1
    if count == 0:
        print("No instances of " + str(letter) + " found in " + str(word))
    else:
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))
    return None


# this took a long time, but also looked back on example code


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


main()

if __name__ == "__main__":
    main()
