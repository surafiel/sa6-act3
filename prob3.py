def find_maximum(numbers, compare):
    
    if not numbers:
        return None

    max_num = numbers[0]

    for num in numbers[1:]:
        max_num = compare(max_num, num)

    return max_num

# Example usage:
numbers = [10, 5, 20, 15, 8, 25]
compare_function = lambda x, y: x if x > y else y
max_number = find_maximum(numbers, compare_function)
print("Maximum number:", max_number)