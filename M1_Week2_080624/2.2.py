def character_count(word):
    character_statistic = {}
    
    # Iterate through each character in the word
    for char in word:
        # Convert the character to lowercase
        char = char.lower()
        # Update the dictionary with the count of the character
        if char in character_statistic:
            character_statistic[char] += 1
        else:
            character_statistic[char] = 1

    return character_statistic

# Test cases
assert character_count("Happiness") == {'h': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
assert character_count("smiles") == {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
assert character_count("Baby") == {'b': 2, 'a': 1, 'y': 1}

# Example usage
print(character_count('smiles'))  # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
print(character_count('Happiness'))  # {'h': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}
