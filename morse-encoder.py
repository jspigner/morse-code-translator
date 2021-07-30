# Create a morse code converter

# Define
def convert_to_morse(code):
    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")
    code = code.replace("A", ".-")
    code = code.replace("B", "-...")
    code = code.replace("C", "-.-.")
    code = code.replace("D", "-..")
    code = code.replace("E", ".")
    code = code.replace("F", "..-.")
    code = code.replace("G", "--.")
    code = code.replace("H", "....")
    code = code.replace("I", "..")
    code = code.replace("J", ".---")
    code = code.replace("K", "-.-")
    code = code.replace("L", ".-..")
    code = code.replace("M", "--")
    code = code.replace("N", "-.")
    code = code.replace("O", "---")
    code = code.replace("P", ".--.")
    code = code.replace("Q", "--.-")
    code = code.replace("R", ".-.")
    code = code.replace("S", "...")
    code = code.replace("T", "-")
    code = code.replace("U", "..-")
    code = code.replace("V", "...-")
    code = code.replace("W", ".--")
    code = code.replace("X", "-..-")
    code = code.replace("Y", "-.--")
    code = code.replace("Z", "--..")
    return code

# Test using numbers
lock_code = "1 2 2 5 0"
print(f"Lock code: {lock_code}")

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")

# Test using letters
# Note that letters are UPPERCASE only
pass_code = " R U M I"
print(f"Pass code: {pass_code}")

morse = convert_to_morse(pass_code)
print(f" Morse code: {morse}")