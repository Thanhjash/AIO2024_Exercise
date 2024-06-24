def max_kernel (numbers, window_size ) :
    result = []

    for start_index in range(len(numbers) - window_size + 1):
        # Extract the current window
        current_window = numbers[start_index:start_index + window_size]
        # Find the maximum in the current window and append to the results list
        result.append(find_max(current_window))
 

    return result


def find_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k = 3
print ( max_kernel ( num_list , k ) )

