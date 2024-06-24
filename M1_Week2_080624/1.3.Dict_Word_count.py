def word_count(file_path):
    word_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()  # Split the line into words
            for word in words:
                word = word.lower()  # Convert each word to lowercase
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    
    return word_dict

def main():
    file_path = 'AIO2024_Exercise\M1_Week2_080624\P1_data.txt' 
    print(word_count(file_path))

if __name__=='__main__':
    main()



