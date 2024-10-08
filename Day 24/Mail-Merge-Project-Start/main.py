PLACEHOLDER = "[name]"

# Read the names from the file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the starting letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # Write the new letter to a new file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)