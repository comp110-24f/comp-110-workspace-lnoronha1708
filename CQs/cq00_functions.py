__author__ = "730766709"


def mimic(message: str) -> str:
    """Take message and repeat it back"""
    return message


def main() -> None:
    """Pull together functions"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
