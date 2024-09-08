from sys import argv


def main():
    NESTED_MORSE = {
        " ": "/ ",
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
    }

    if len(argv) != 2:
        print("AssertionError: the arguments are bad")
        exit(1)

    try:
        input_str = str(argv[1])
        output_str = ""
        for c in input_str:
            output_str += NESTED_MORSE[c.upper()] + " "
        print(output_str.strip())

    except Exception:
        print("AssertionError: the arguments are bad")
        exit(1)


if __name__ == '__main__':
    main()
