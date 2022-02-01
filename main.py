print("Welcome to the Text to Morse Code Converter CLI")

# Write letter (key) to morse code (value) dict
text_to_morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
                           'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
                           'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
                           'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                           'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
                           'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                           '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                           '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
                           '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
                           ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
                           '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': "/"}

# Get input in plain text - all lowercase
plain_text = input("Please insert text for transformation into morse code: ").lower()

# Iterate through each character in input for conversion to morse code - Encrypt
morse_code = [text_to_morse_dict[char] for char in plain_text]

# Transform list with each character of morse into string
result = " ".join(morse_code)
print(f"The morse code of the inputted text is: {result}")
