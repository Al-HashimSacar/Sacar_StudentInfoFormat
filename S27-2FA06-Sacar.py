# Version 1: Basic input and output without formatting

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

full_name = first_name + " " + last_name

print("\nFormatted Output:")
print("Name:", full_name)
print("Name Code:", full_name)
print("Section:", section)
print("Favorite Subject:", favorite_subject)
print("Character Count:", len(full_name))

# Version 2: Added string manipulation methods for proper formatting

# Get inputs and remove accidental leading/trailing spaces
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# Combine and format strings
full_name = f"{first_name} {last_name}".title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()
character_count = len(full_name)

# Display final formatted output
print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {character_count}")
