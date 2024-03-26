import re


def seperateNos(word):
        s = re.sub(r'\d', '', word)
        highest_odd = None
        for char in s:
            if char.isdigit():
                continue
            if char.isnumeric():
                num = int(char)
                if num % 2 != 0:
                    if highest_odd is None or num > highest_odd:
                        highest_odd = num

        return highest_odd



string_with_digits = "abc123def456ghi789jkl"
highest_odd = seperateNos(string_with_digits)
print("Highest odd number:", highest_odd)


def remove_digits_and_find_highest_odd(s):
    # Remove digits from the string
    s = re.sub(r'\d', '', s)

    # Initialize variable to store the highest odd number
    highest_odd = None

    # Print the characters left after removing digits
    print("Characters after removing digits:", s)

    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a valid digit (0-9)
        if char.isnumeric():
            num = int(char)
            # Check if the number is odd
            if num % 2 != 0:
                # Update the highest odd number if necessary
                if highest_odd is None or num > highest_odd:
                    highest_odd = num

    return highest_odd


# Example usage
string_with_digits = "abc123def456ghi789jkl"
highest_odd = remove_digits_and_find_highest_odd(string_with_digits)
print("Highest odd number:", highest_odd)


def find_highest_odd_number(s):
    highest_odd = None
    current_number = ""

    for char in s:
        if char.isdigit():
            current_number += char
            #print(current_number)
        elif current_number:
            num = int(current_number)
            if num % 2 != 0 and (highest_odd is None or num > highest_odd):
                highest_odd = num
            current_number = ""

    if current_number:
        num = int(current_number)
        if num % 2 != 0 and (highest_odd is None or num > highest_odd):
            highest_odd = num

    return highest_odd

string = "123hjh22 hh243"
highest_odd = find_highest_odd_number(string)
print("Highest odd number:", highest_odd)