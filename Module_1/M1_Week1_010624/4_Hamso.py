import numpy as np
import math

def factorial(n):
    """Calculates the factorial of a positive integer n."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    return 1 if n == 0 else n * factorial(n - 1)

def estimate_sin(x, n):
    """Estimates sin(x) using the Taylor series with NumPy."""
    terms = np.array([(-1)**i * x**(2*i + 1) / math.factorial(2*i + 1) for i in range(n)])
    return np.sum(terms, axis=0)

def estimate_cos(x, n):
    """Estimates cos(x) using the Taylor series with NumPy."""
    terms = np.array([(-1)**i * x**(2*i) / math.factorial(2*i) for i in range(n)])
    return np.sum(terms, axis=0)

def estimate_sinh(x, n):
    """Estimates sinh(x) using the Taylor series with NumPy."""
    return estimate_sin(x * 1j, n).imag

def estimate_cosh(x, n):
    """Estimates cosh(x) using the Taylor series with NumPy."""
    return estimate_cos(x * 1j, n).real

def get_and_validate_input():
    """Gets input from the user and validates it."""
    while True:
        try:
            x_str = input("Enter the value of x (in radians): ")
            x = float(x_str)  # Attempt to convert to float

            n_str = input("Enter the number of terms (positive integer): ")
            n = int(n_str)   # Attempt to convert to int

            if n <= 0:
                raise ValueError("n must be a positive integer.")

            return x, n

        except ValueError:
            print("Invalid input: Please enter a number for x and a positive integer for n.")


# Main program logic
if __name__ == "__main__":
    x_values, n = get_and_validate_input()
    x_values = np.array([x_values])  # Create a NumPy array

    sin_approximations = estimate_sin(x_values, n)
    cos_approximations = estimate_cos(x_values, n)
    sinh_approximations = estimate_sinh(x_values, n)
    cosh_approximations = estimate_cosh(x_values, n)

    print("sin approximations:", sin_approximations[0])
    print("cos approximations:", cos_approximations[0])
    print("sinh approximations:", sinh_approximations[0])
    print("cosh approximations:", cosh_approximations[0])
