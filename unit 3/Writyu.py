# Mapping from each key to its left neighbor on the QWERTY keyboard
keyboard = {
    '1': '`', '2': '1', '3': '2', '4': '3', '5': '4',
    '6': '5', '7': '6', '8': '7', '9': '8', '0': '9',
    '-': '0', '=': '-', 
    'W': 'Q', 'E': 'W', 'R': 'E', 'T': 'R', 'Y': 'T',
    'U': 'Y', 'I': 'U', 'O': 'I', 'P': 'O', '[': 'P',
    ']': '[', '\\': ']', 
    'S': 'A', 'D': 'S', 'F': 'D', 'G': 'F', 'H': 'G',
    'J': 'H', 'K': 'J', 'L': 'K', ';': 'L', "'": ';', 
    'X': 'Z', 'C': 'X', 'V': 'C', 'B': 'V', 'N': 'B',
    'M': 'N', ',': 'M', '.': ',', '/': '.'
}

# Read multiple lines of input
try:
    while True:
        line = input()
        decoded_line = ""
        for char in line:
            if char == ' ':
                decoded_line += ' '
            else:
                decoded_line += keyboard.get(char, char)  # Default to char if not in map
        print(decoded_line)
except EOFError:
    pass
