import sys

def load_ascii_art(file_path):
    ascii_art = {}
    ascii_index = 31 
    current_art = []

    with open(file_path, "r") as file:
        for line in file:
            if line.strip() == "": 
                if current_art:
                    ascii_art[ascii_index] = current_art
                    current_art = []
                    ascii_index += 1
            else:
                current_art.append(line.rstrip("\n"))

        if current_art:
            ascii_art[ascii_index] = current_art

    return ascii_art

def generate_ascii_art(word, ascii_art):
    if not word:
        return []

    words = word.split("\n")
    max_height = 8  
    all_results = []

    dollar_art = None
    if 36 in ascii_art: 
        dollar_art = ascii_art[36]
        if len(dollar_art) < max_height:
            padding_top = max_height - len(dollar_art)
            dollar_art = [" " * len(dollar_art[0])] * padding_top + dollar_art

    i = 0
    while i < len(words):
        current_word = words[i]
        
        if current_word:
            result_lines = [""] * max_height

            for char in current_word:
                if char == " ":
                    for j in range(max_height):
                        result_lines[j] += " " * 5
                else:
                    ascii_value = ord(char)
                    if char.isdigit():
                        ascii_value -= 2

                    if not char.isalnum():  
                        ascii_value -= 0

                    if ascii_value in ascii_art:
                        char_art = ascii_art[ascii_value]
                        char_height = len(char_art)

                        if char_height <= 7:
                            padding_top = 6 - char_height
                            char_art = [" " * len(char_art[0])] * padding_top + char_art
                        else:
                            char_art = char_art + [" " * len(char_art[0])] * (max_height - char_height)

                        for j in range(max_height):
                            result_lines[j] += char_art[j] if j < len(char_art) else " " * len(char_art[0])
                    else:
                        print(f"Warning: Character '{char}' not found in ASCII art.", file=sys.stderr)
                        for j in range(max_height):
                            result_lines[j] += " " * 5

            all_results.extend(result_lines)

            if i + 1 < len(words):  
                if words[i + 1] == "":
                    if i + 2 < len(words) and words[i + 2] == "": 
                        if dollar_art:
                            all_results.extend(dollar_art)
                        i += 2 
                    else:  
                        all_results.append("")  
                        i += 1 
                else:  
                    all_results.append("") 
            
        i += 1

    return all_results


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <word>")
        sys.exit(1)

    raw_input = sys.argv[1]
    processed_input = raw_input.encode().decode("unicode_escape")

    if processed_input == "":
        sys.exit(0)
    if processed_input == "\n":
        print()
        sys.exit(0)

    ascii_art = load_ascii_art("standard.txt")
    result = generate_ascii_art(processed_input, ascii_art)

    for line in result:
        print(line)


if __name__ == "__main__":
    main()
