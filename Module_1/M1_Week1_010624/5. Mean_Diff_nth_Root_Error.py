import numpy as np

def mdre_loss(y_true, y_hat, n, p=1):
    """Calculates the Mean Difference of nth Root Error (MDRE) loss.

    Args:
        y_true: The array of true values.
        y_hat: The array of predicted values.
        n: The root to use (e.g., 2 for square root, 3 for cube root).
        p: The power to raise the relative errors to in the loss function (default is 1).

    Returns:
        The MDRE loss value.

    Raises:
        ValueError: If n is less than or equal to zero.
        ValueError: If y_true and y_hat have different shapes.
        ValueError: If n is even and any element in y_true or y_hat is negative.
    """

    if n <= 0:
        raise ValueError("n must be a positive integer.")

    y_true = np.asarray(y_true)
    y_hat = np.asarray(y_hat)

    if y_true.shape != y_hat.shape:
        raise ValueError("y_true and y_hat must have the same shape.")

    # Check for negative values and even root
    if n % 2 == 0 and (np.any(y_true < 0) or np.any(y_hat < 0)):
        raise ValueError("Cannot calculate even nth root for negative numbers in y_true or y_hat.")

    # Calculate nth root of absolute values (no sign needed)
    y_true_root = np.abs(y_true)**(1/n)
    y_hat_root = np.abs(y_hat)**(1/n)

    # Handle potential division by zero (avoid NaNs)
    with np.errstate(divide='ignore', invalid='ignore'):
        absolute_errors = np.abs(y_true_root - y_hat_root)
        relative_errors = np.where(y_true_root != 0, absolute_errors / np.abs(y_true_root), 0)

    # Raise relative errors to the power p
    relative_errors_p = np.power(relative_errors, p)

    # Calculate MDRE loss
    mdre_loss_value = np.mean(relative_errors_p)

    return mdre_loss_value

def get_float_list(prompt):
    """Gets a list of float values from user input."""
    while True:
        try:
            user_input = input(prompt)
            return list(map(float, user_input.split()))
        except ValueError:
            print("Please enter valid numbers separated by spaces.")

def get_positive_int(prompt):
    """Gets a positive integer from user input."""
    while True:
        try:
            value = input(prompt)
            if value == '':
                return None
            value = int(value)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    while True:
        y_true = get_float_list("Enter the true values (space-separated): ")
        y_hat = get_float_list("Enter the predicted values (space-separated): ")
        
        if len(y_true) != len(y_hat):
            print("Error: The number of true values and predicted values must be the same.")
            continue

        n = get_positive_int("Enter the root to use: ")
        if n is None:
            print("Error: The root must be a positive integer.")
            continue

        p = get_positive_int("Enter the power to raise the relative errors to (default is 1): ")
        if p is None:
            p = 1

        try:
            mdre_loss_value = mdre_loss(y_true, y_hat, n, p)
            print("MDRE Loss:", mdre_loss_value)
        except ValueError as e:
            print(f"Error: {e}")
            continue
        
        restart = input("Do you want to start again? (yes to restart, any other key to exit): ").strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()

