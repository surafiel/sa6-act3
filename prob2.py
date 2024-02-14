strings = ["banana", "apple", "orange", "kiwi", "grape", "melon", "pear", "apricot"]
sorted_strings = sorted(strings, key=lambda x: (len(x), x))
print("Sorted strings:", sorted_strings)