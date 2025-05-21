def count_letters_and_digits():
    sentence = input("Enter a text: ")
    letters = 0
    digits = 0
    invalid = 0
    for letter in sentence:
        if letter.isalpha():
            letters += 1
        elif letter.isdigit():
            digits += 1
        else:
            invalid += 1
    print(f"LETTERS:----|{letters}|------")
    print(f"DIGITS:-----|{digits}|------")
    print(f"INVALID CHARACTERS:-----|{invalid}|------")
count_letters_and_digits()
print("there are certain words")