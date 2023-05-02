# decode morse code character
def decode_char(letter):
    # dictionary
    dictionary = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
    }

    for key in dictionary:
        if letter == dictionary.get(key):
            return key


def decode_word(word):
    split_word = word.split()

    word_array = []
    for letter in split_word:
        word_array.append(decode_char(letter))

    return "".join(word_array)


# decode entire message
def decode_msg(message):
    words = message.split("  ")
    decoded_message = ""
    for word in words:
        decoded_message += f"{decode_word(word)} "
    return decoded_message


# The example below should print out "A BOX FULL OF RUBIES"
print(decode_msg(".-   -... --- -..-   ..-. ..- .-.. .-..   --- ..-.   .-. ..- -... .. . ..."))
