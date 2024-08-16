import math

def relu(x):
    return max(0, x)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def elu(x, alpha):
    return x if x > 0 else alpha * (math.exp(x) - 1)

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def get_input(prompt):
    while True:
        value = input(prompt)
        if is_number(value):
            return float(value)
        else:
            print("x must be a number. Please try again.")

def get_choice():
    valid_choices = {"sigmoid", "relu", "elu"}
    while True:
        choice = input("Input activation function (sigmoid|relu|elu): ").lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please choose from sigmoid, relu, or elu.")

def main():
    while True:
        x = get_input("Enter input x to calculate: ")
        choice = get_choice()
        
        if choice == "sigmoid":
            y = sigmoid(x)
        elif choice == "relu":
            y = relu(x)
        elif choice == "elu":
            alpha = get_input("Enter alpha for ELU function: ")
            y = elu(x, alpha)
        
        print(f"{choice}: f({x}) = {y}")

        continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
