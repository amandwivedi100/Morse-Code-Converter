morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def convert_to_alpha(text: str) -> str:
    inverted_morse_code_dict: dict[str, str] = {value: key for key, value in morse_code_dict.items()}
    characters = text.split()
    result = ''
    for character in characters:
        if character == '/':
            result += ' '
        else:
            result += inverted_morse_code_dict.get(character, '')
    return result


def main() -> None:
    question: str = input('Do you want to enter the text? (Yes/no): ').lower().strip()
    if question == 'yes':
        user_input: str = input('Enter Text: ')
        output: str = convert_to_morse(user_input)
        print(output)
    else:
        morse_input: str = input("Please enter the morse code: ")
        print(convert_to_alpha(morse_input))




if __name__ == '__main__':
    main()


"""
1. Edit the program so that it also works with symbols.
2. Create a function that can convert the morse code back into regular text.
"""
