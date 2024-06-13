def find_max_in_sliding_windows(numbers, window_size):
    max_values = []

    # Iterate through the list with the sliding window of the specified size
    for start_index in range(len(numbers) - window_size + 1):
        # Extract the current window
        current_window = numbers[start_index:start_index + window_size]
        # Find the maximum in the current window and append to the results list
        max_values.append(find_max(current_window))

    return max_values

def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

def main():
    num_list = []
    n = int(input("Enter the number of elements in the list: "))

    for i in range(n):
        while True:
            try:
                num = int(input(f"Enter element {i + 1}: "))
                num_list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    while True:
        try:
            window_size = int(input("Enter the size of the sliding window: "))
            if window_size < 1:
                print("Error: window size should be greater than or equal to 1")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    max_values_in_windows = find_max_in_sliding_windows(num_list, window_size)
    print("Maximum values in each window of size", window_size, ":", max_values_in_windows)

if __name__ == "__main__":
    main()
