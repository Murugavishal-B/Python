# Input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find common characters
common_chars = set(string1) & set(string2)

# Count common characters
common_count = len(common_chars)

# Display results
print(f"Common characters: {''.join(sorted(common_chars))}")
print(f"Count of common characters: {common_count}")
