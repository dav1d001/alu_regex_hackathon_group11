import re

def match_isbn_number():
    isbn_pattern = r"ISBN \d{3}-\d-\d{3}-\d{5}-\d"

    input_string = input("Enter an ISBN number: ")

    # This matches against the regular expression pattern
    isbn_match = re.match(isbn_pattern, input_string)

    if isbn_match:
        isbn_number = isbn_match.group()
        print("Valid ISBN Number:", isbn_number)
    else:
        print("Invalid ISBN Number")

# Lastly, we call the function
match_isbn_number()
