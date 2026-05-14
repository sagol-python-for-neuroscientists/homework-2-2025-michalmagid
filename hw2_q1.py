MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }

def word_to_morse(word: str) -> str:
    return "".join(MORSE_CODE.get(c, "") for c in word)

def line_to_morse(line: str) -> str:
    return "\n".join(word_to_morse(word) for word in line.split())


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    with open(input_file) as file:
        text = file.read().upper()

    result = "\n".join(line_to_morse(line) for line in text.splitlines())

    with open(output_file, "w") as file:
        file.write(result)

if __name__ == "__main__":
    english_to_morse()