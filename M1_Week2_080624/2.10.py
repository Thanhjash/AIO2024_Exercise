def My_function(integers, number=1):
    comparison_list = [i == number for i in integers]
    return any(comparison_list)

my_list = [1, 3, 9, 4]
assert My_function(my_list, -1) == False

my_list = [1, 2, 3, 4]
print(My_function(my_list, 2))
