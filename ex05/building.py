import sys


def argv_security_check(argv: list) -> None:
    """
    Check if the amount arguments is correct
    :param argv:
    :return:
    """
    if len(argv) > 2:
        raise AssertionError("more than one argument is provided")


def analyze_text(text: str) -> None:
    """
    Analyze the text and count the number of characters, upper letters,
    lower letters, punctuation marks, spaces, and digits.
    :param text: The text to be analyzed.
    :return: None
    """
    punctuation = ".,:;!?-'\"()[]{}<>/\\|_*&^%$#@`~+=()"

    total_chars = len(text)
    total_upper_letters = sum(1 for c in text if c.isupper())
    total_lower_letters = sum(1 for c in text if c.islower())
    total_punctuation = sum(1 for c in text if c in punctuation)
    total_spaces = sum(1 for c in text if c.isspace())
    total_digits = sum(1 for c in text if c.isdigit())

    print("The text contains", total_chars, "characters:")
    print("-", total_upper_letters, "upper letters")
    print("-", total_lower_letters, "lower letters")
    print("-", total_punctuation, "punctuation marks")
    print("-", total_spaces, "spaces")
    print("-", total_digits, "digits")


def main():
    try:
        argv_security_check(sys.argv)

        if len(sys.argv) == 1:
            input_str = input("What is the text to count?\n")
        else:
            input_str = sys.argv[1]

        analyze_text(input_str)

    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
    except Exception as error:
        print("Error:", error)


if __name__ == '__main__':
    main()
