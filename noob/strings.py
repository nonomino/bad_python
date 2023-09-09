# A string of 24 characters
my_string = "HelloandWelcometoPython"

# Length of the string
length = len(my_string)
print("Length:", length)

# Convert to uppercase
uppercase = my_string.upper()
print("Uppercase:", uppercase)

# Convert to lowercase
lowercase = my_string.lower()
print("Lowercase:", lowercase)

# Capitalize the first letter
capitalized = my_string.capitalize()
print("Capitalized:", capitalized)

# Count occurrences of a substring
count = my_string.count("o")
print("Count of 'o':", count)

# Find the index of a substring (case-sensitive)
index = my_string.find("Welcometo")
print("Index of 'Welcometo':", index)

# Replace a substring
replaced = my_string.replace("Python", "Programming")
print("Replaced:", replaced)

# Check if string starts with a prefix
starts_with = my_string.startswith("Hello")
print("Starts with 'Hello':", starts_with)

# Check if string ends with a suffix
ends_with = my_string.endswith("Python")
print("Ends with 'Python':", ends_with)

# Split the string into a list of substrings
split_list = my_string.split("and")
print("Split list:", split_list)

# Join a list of strings into one string
joined = "and".join(split_list)
print("Joined:", joined)

# Strip 'H', 'n', and 'o' characters from both ends
stripped = my_string.strip("Hno")
print("Stripped:", stripped)

# Get a substring using slicing
substring = my_string[5:12]
print("Substring:", substring)

# Reverse the string using slicing
reversed_string = my_string[::-1]
print("Reversed:", reversed_string)

# Check if all characters are alphabetic
is_alpha = my_string.isalpha()
print("Is alphabetic:", is_alpha)

# Check if all characters are digits
is_digit = my_string.isdigit()
print("Is digit:", is_digit)
