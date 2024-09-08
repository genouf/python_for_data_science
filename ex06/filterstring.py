from sys import argv, exit
from ft_filter import ft_filter


def len_is_ok(word: str, length: int) -> bool:
    """
    Check if the length of the word is greater than or equal to the length.
    :param word: The word to check.
    :param length: The length to compare.
    :return: True if the length of the word
    is greater than or equal to the length, False otherwise.
    """
    return len(word) >= length


def main():

    try:
        if (len(argv) != 3):
            print("AssertionError: the arguments are bad")
            exit(1)

        words = argv[1].split()
        words = list(ft_filter(lambda x: len_is_ok(x, int(argv[2])), words))
        print(words)
    except Exception:
        print("AssertionError: the arguments are bad")
        exit(1)


if __name__ == '__main__':
    main()
