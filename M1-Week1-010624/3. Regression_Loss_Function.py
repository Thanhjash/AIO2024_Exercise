import numpy as np

def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def root_mean_squared_error(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def get_input(prompt):
    while True:
        value = input(prompt)
        if is_number(value) and float(value) > 0 and float(value).is_integer():
            return int(float(value))
        else:
            print("Number of samples must be a positive integer.")

def get_choice():
    valid_choices = {"mae", "mse", "rmse"}
    while True:
        choice = input("Input loss name (MAE|MSE|RMSE): ").lower()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please choose from MAE, MSE, or RMSE.")

def main():
    while True:
        n_samples = get_input("Enter number of samples to calculate: ")
        # Generate random true values and predicted values
        np.random.seed(0)  # For reproducibility
        y_true = np.random.rand(n_samples)
        y_pred = np.random.rand(n_samples)
        print("\nTrue values:", y_true)
        print("Predicted values:", y_pred)

        choice = get_choice()
        
        if choice == "mae":
            y = mean_absolute_error(y_true, y_pred)
            print(f"\nMean Absolute Error (MAE): {y}")
        elif choice == "mse":
            y = mean_squared_error(y_true, y_pred)
            print(f"Mean Squared Error (MSE): {y}")
        elif choice == "rmse":
            y = root_mean_squared_error(y_true, y_pred)
            print(f"Root Mean Squared Error (RMSE): {y}")        

        continue_choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
