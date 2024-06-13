def levenshtein(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    # Create a matrix of size len_str1 x len_str2 initialized to 0
    matrix = [[0 for n in range(len_str2)] for m in range(len_str1)]

    # Initialize the first row and column of the matrix
    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i-1][j] + 1,       # Deletion
                               matrix[i][j-1] + 1,       # Insertion
                               matrix[i-1][j-1] + cost)  # Substitution

    # Return the value in the bottom-right cell, which is the Levenshtein distance
    return matrix[len_str1-1][len_str2-1]

def main():
    while True:
        str1 = input("Input string 1: ")
        str2 = input("Input string 2: ")
        distance = levenshtein(str1, str2)
        print("The minimum number of single-character edits: ", distance)

        # Prompt user to continue or exit
        choice = input("Do you want to continue? (yes to continue, any other key to exit): ").strip().lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()
