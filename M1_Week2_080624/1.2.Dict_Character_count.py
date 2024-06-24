def count_letters(word):
    letter_dict = {}
    for letter in word:
        letter = letter.lower()
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def main():
    word = input("Input your word: ")
    print("Letter counts:", count_letters(word))

if __name__ == "__main__":
    main()
