def raise_to_power(numbers, n):
    
    powered_numbers = list(map(lambda x: x**n, numbers))
    return powered_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5]
n = 3
powered_numbers = raise_to_power(numbers, n)
print("Powered numbers:", powered_numbers)